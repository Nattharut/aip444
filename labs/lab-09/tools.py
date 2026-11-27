import os
import re
from dataclasses import dataclass, field
from datetime import date
from typing import Literal

import requests
from agents import RunContextWrapper, function_tool
from pydantic import BaseModel, Field
from tavily import TavilyClient

# Characters of a page returned per read_url call. Long pages are paged with
# `start`, so the agent can still reach author bios and reference lists at the
# bottom without every read costing 30,000+ characters of context.
READ_LIMIT = 10_000
READ_TIMEOUT_SECONDS = 60
SEARCH_RESULTS = 5

TARGET_ERROR = re.compile(r"^Warning: Target URL returned error (\d+)", re.MULTILINE)
BOT_CHECK = re.compile(
    r"^Title: (Just a moment\.\.\.|Checking your browser|Attention Required|.*reCAPTCHA)", re.MULTILINE | re.IGNORECASE
)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPORTS_DIR = os.path.join(SCRIPT_DIR, "reports")


def tool_error(ctx, error):
    # The SDK's default message gives no reason, so the model could not tell
    # which field of a rejected assess_credibility call to fix (for example
    # transparency_score=7) and kept repeating it.
    detail = " ".join(f"{type(error).__name__}: {error}".split())[:800]
    return f"Error: {detail}. Fix the arguments and call the tool again."


@dataclass
class RunInfo:
    """Per-run state shared with the tools through the SDK's run context."""

    require_assessment: bool = True
    assessment: dict | None = None
    reports: list[str] = field(default_factory=list)
    # Requested file name -> path actually written in this run.
    saved_as: dict[str, str] = field(default_factory=dict)
    _tavily: TavilyClient | None = None

    @property
    def tavily(self):
        if self._tavily is None:
            self._tavily = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])
        return self._tavily


# ---------------------------------------------------------------------------
# read_url


def fetch_markdown(url):
    """Return (markdown, error). error is None on success, else a message for the agent."""
    try:
        response = requests.get(f"https://r.jina.ai/{url}", timeout=READ_TIMEOUT_SECONDS)
    except requests.RequestException as err:
        return None, f"could not reach the Jina Reader ({type(err).__name__})."

    if response.status_code == 429:
        return None, "the reader is rate-limited (HTTP 429). Wait for other work, then try once more, or use search results instead."
    if response.status_code != 200:
        # Jina explains failures of the target site (403, 404, 451, timeouts)
        # in a JSON body with a readableMessage.
        try:
            detail = response.json().get("readableMessage") or response.json().get("message")
        except ValueError:
            detail = response.text[:300]
        return None, f"HTTP {response.status_code}. {detail or ''}".strip()

    text = response.text
    # Jina answers 200 even when the target site failed, with a warning line
    # (seen for a GitHub 404), and bot checks (PubMed's reCAPTCHA, Cloudflare's
    # "Just a moment...") arrive as ordinary pages. Both looked like successful
    # reads to the agent, so they are reported as errors instead.
    target_error = TARGET_ERROR.search(text[:2000])
    if target_error:
        return None, f"the site returned HTTP {target_error.group(1)}."
    if BOT_CHECK.search(text[:2000]):
        return None, "the site showed a CAPTCHA or bot check instead of the page."
    if len(text.strip()) < 200:
        return None, "the page returned almost no text (it may need JavaScript, be a login wall, or be empty)."
    return text, None


@function_tool(failure_error_function=tool_error)
def read_url(url: str, start: int) -> str:
    """Read a web page and return its content as Markdown.

    Use it for the source being evaluated, its About, editorial policy or author pages,
    and articles found by web_search that may corroborate or contradict its claims.

    Args:
        url: The full URL to read, starting with http:// or https://.
        start: Character offset to start reading from. Use 0 the first time; the end of a long page says which value reads the next part.
    """
    if not url.startswith(("http://", "https://")):
        return f"Error: {url!r} is not a full URL. Pass one that starts with https://."

    text, error = fetch_markdown(url)
    if error:
        return (
            f"Error: could not read {url}: {error} Do not retry this URL more than once. "
            "Try another page on the same site or search for the title, and note the gap in your report."
        )

    start = max(0, start)
    if start >= len(text):
        return f"Error: start={start} is past the end of the page ({len(text):,} characters)."
    end = min(start + READ_LIMIT, len(text))
    part = text[start:end]
    if end < len(text):
        part += (
            f"\n\n[Showing characters {start:,}-{end:,} of {len(text):,}. "
            f"Call read_url with start={end} to read the next part.]"
        )
    elif start > 0:
        part += f"\n\n[End of page. Showed characters {start:,}-{end:,} of {len(text):,}.]"
    return part


# ---------------------------------------------------------------------------
# web_search


@function_tool(failure_error_function=tool_error)
def web_search(ctx: RunContextWrapper[RunInfo], query: str) -> str:
    """Search the web. Returns up to 5 results with title, URL, date and an excerpt.

    Use it to research the author and the publication, to find independent sources
    that corroborate or contradict the source's claims, and to find fact-checks,
    retractions or the primary sources the article relies on.

    Args:
        query: The search query. Put names and exact titles in quotes when you need an exact match.
    """
    try:
        response = ctx.context.tavily.search(query=query, search_depth="basic", max_results=SEARCH_RESULTS)
    except Exception as err:
        # Covers a used-up quota, a bad key, rate limits and network errors.
        # The agent is told to carry on and report the check it could not do.
        return f"Error: the search failed ({type(err).__name__}: {err}). Continue with what you have and mention the failed check in the report."

    results = response.get("results", [])
    if not results:
        return f'No results for "{query}". Try different words, or record that you found no evidence.'
    lines = [f'Search results for "{query}" (searched {date.today().isoformat()}):']
    for i, r in enumerate(results, 1):
        lines.append("")
        lines.append(f"[{i}] {r.get('title') or '(untitled)'}")
        lines.append(f"URL: {r['url']}")
        if r.get("published_date"):
            lines.append(f"Published: {r['published_date']}")
        lines.append(f"Excerpt: {(r.get('content') or '').strip()}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# assess_credibility: the "think" tool. Its schema is the credibility rubric.

SourceType = Literal[
    "peer_reviewed_journal",
    "news_organization",
    "government_agency",
    "nonprofit_organization",
    "corporate_blog",
    "personal_blog",
    "social_media",
    "wiki",
    "unknown",
]


class Author(BaseModel):
    name: str = Field(
        description="The author's name as found on the page or elsewhere. If it is still unknown after "
        "checking the byline, metadata, About/Team pages and searching the title, write 'Unknown' and "
        "list what you checked."
    )
    credentials: str = Field(
        description="Qualifications, job, affiliation and other work on this topic that you found, with where you "
        "found them. If you found nothing, describe what you searched for. Make sure it is the same person, not "
        "someone with the same name."
    )
    credibility_assessment: str = Field(
        description="How much the author's expertise supports trusting this source. If the author is unknown, "
        "explain how that affects the overall assessment."
    )


class Publication(BaseModel):
    name: str = Field(description="Publication, organization or website name. If it is not a recognized outlet, use the domain name.")
    reputation: str = Field(
        description="What your research found about the publication: who runs or owns it, its track record, any "
        "known problems (predatory journal, misinformation, corrections). If unknown, describe what you searched for."
    )
    editorial_process: Literal["peer_reviewed", "editor_reviewed", "self_published", "unknown"] = Field(
        description="How content is reviewed before it is published, based on an editorial policy, masthead, "
        "journal information or the platform. Use 'unknown' if you found no evidence."
    )


class ClaimCheck(BaseModel):
    claim: str = Field(description="One main claim from the source, in a single sentence.")
    status: Literal["corroborated", "contradicted", "no_evidence_found", "not_checked"] = Field(
        description="'corroborated' only if an independent credible source says the same; 'contradicted' only if a "
        "credible source says otherwise; 'no_evidence_found' if you looked and found nothing either way."
    )
    evidence: str = Field(description="The sources (with URLs) behind the status, or what you searched for if you found nothing.")


class ContentAnalysis(BaseModel):
    claims_checked: list[ClaimCheck] = Field(description="The 2 to 4 main claims of the source and what your verification found for each.")
    claims_supported_by_evidence: bool = Field(description="Are the main claims backed by data, citations or primary sources in the source itself?")
    sources_cited: bool = Field(description="Does the source cite or link its sources?")
    corroborated_by_other_sources: bool = Field(description="Did you find other credible, independent sources reporting the same main claims?")
    contradicted_by_other_sources: bool = Field(description="Did you find credible sources that contradict the main claims?")
    primary_vs_secondary: Literal["primary_source", "secondary_source", "tertiary_source"] = Field(
        description="primary: original research, data or official statement; secondary: reports on or analyses "
        "primary sources; tertiary: summarizes secondary sources (encyclopedias, listicles)."
    )
    funding_or_sponsorship: str = Field(
        description="Who funds the publication or the research, sponsors, advertisers or products being sold, as far "
        "as you could find. Say 'Not found' with what you checked if unknown."
    )
    bias_and_tone: str = Field(
        description="Is the language neutral or emotional, does it inform or persuade, are counterarguments and "
        "limitations acknowledged, and is there a commercial or political interest?"
    )
    date_published: str = Field(
        description="Publication date and last-updated date if shown, and whether the information is still current "
        "for the topic as of today. 'Unknown' if no date was found."
    )


class CredibilityAssessment(BaseModel):
    source_url: str = Field(description="The URL being evaluated.")
    source_type: SourceType = Field(description="What kind of source this is.")
    author: Author = Field(description="What you found out about who wrote the source.")
    publication: Publication = Field(description="What you found out about where the source was published.")
    content_analysis: ContentAnalysis = Field(
        description="The source's main claims, evidence, independence, bias and date, as checked in this investigation."
    )
    transparency_score: int = Field(
        ge=1,
        le=5,
        description="1-5: how open the source is about who wrote it, how the information was produced (methods, "
        "sources) and who funds it. 5 = all three are clear; 1 = none are.",
    )
    overall_credibility: Literal["high", "medium", "low", "very_low"] = Field(
        description="Overall credibility for use in an academic research report."
    )
    reasoning: str = Field(
        description="Why you chose this rating, citing specific evidence you found (and what you could not find)."
    )
    evidence_urls: list[str] = Field(
        description="Every URL you read or got search results from that this assessment relies on. Only URLs that "
        "appeared in this investigation."
    )


@function_tool(failure_error_function=tool_error)
def assess_credibility(ctx: RunContextWrapper[RunInfo], evaluation: CredibilityAssessment) -> dict:
    """Record your structured credibility assessment of the source.

    This tool has no side effects. Call it after you have read the source and investigated
    the author, the publication and the main claims, and before you write the report.
    Fill every field from evidence you actually found; where something is unknown, say
    what you checked.

    Args:
        evaluation: The complete structured assessment.
    """
    ctx.context.assessment = evaluation.model_dump()
    return {"status": "evaluation_recorded", "evaluation": ctx.context.assessment}


# ---------------------------------------------------------------------------
# save_report


def safe_filename(name):
    # The agent picks the name, so keep it to one plain file inside reports/.
    stem = os.path.basename(name.strip())
    stem = re.sub(r"\.md$", "", stem, flags=re.IGNORECASE)
    stem = re.sub(r"[^A-Za-z0-9._-]+", "-", stem).strip(".-")[:80]
    return (stem or "credibility-report") + ".md"


@function_tool(failure_error_function=tool_error)
def save_report(ctx: RunContextWrapper[RunInfo], filename: str, markdown: str) -> str:
    """Save the final credibility report as a Markdown file in the reports folder.

    Args:
        filename: File name for the report, lowercase with hyphens, e.g. 'cbc-housing-prices.md'.
        markdown: The complete Markdown report.
    """
    if ctx.context.require_assessment and ctx.context.assessment is None:
        return "Error: call assess_credibility with your structured assessment before saving the report."
    if not markdown.strip():
        return "Error: the report is empty."

    os.makedirs(REPORTS_DIR, exist_ok=True)
    name = safe_filename(filename)
    # A second save under the same name in one run replaces that run's report.
    # A file left by an earlier run is kept (the first CBC report was lost
    # that way), so the new one gets a numbered name.
    path = ctx.context.saved_as.get(name)
    if path is None:
        path = os.path.join(REPORTS_DIR, name)
        stem, n = path[:-3], 2
        while os.path.exists(path):
            path, n = f"{stem}-{n}.md", n + 1
        ctx.context.saved_as[name] = path
        ctx.context.reports.append(path)
    with open(path, "w", encoding="utf-8") as f:
        f.write(markdown.rstrip() + "\n")
    return f"Saved the report to reports/{os.path.basename(path)} ({len(markdown):,} characters)."
