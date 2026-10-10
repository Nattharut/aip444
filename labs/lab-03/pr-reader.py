#!/usr/bin/env python3
import os
import re
import sys
from datetime import datetime
from html import escape
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI, APIError, APIStatusError

STUDENT_NAME = "Nattharut Natvongsakul"
STUDENT_ID = "184108231"

# Free instruction-tuned model first; paid version of the same model if the free
# one is rate-limited (429) or otherwise unavailable.
DEFAULT_MODEL = "google/gemma-4-31b-it:free"
FALLBACK_MODEL = "google/gemma-4-31b-it"

TEMPERATURE = 0.3
MAX_TOKENS = 4000
REQUEST_TIMEOUT_SECONDS = 180

# Arbitrary cap so one huge PR can't eat the model's whole context window.
# Characters, not tokens.
DIFF_LIMIT = 95_000

GITHUB_HEADERS = {
    "User-Agent": "AIP444-Lab-03",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2026-03-10",
}

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SYSTEM_PROMPT_PATH = os.path.join(SCRIPT_DIR, "SYSTEM_PROMPT.md")


def print_header():
    run_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("AIP444 Fall 2026 - Lab 03")
    print(f"pr-reader: Developed by {STUDENT_NAME} - {STUDENT_ID}")
    print(f"Run Date: {run_date}")
    print("-" * 60)


def load_api_key():
    load_dotenv(find_dotenv())
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        print("❌ Error: OPENROUTER_API_KEY not found")
        sys.exit(1)
    return api_key


def parse_pr_url(url):
    """Return (owner, repo, number) from https://github.com/OWNER/REPO/pull/NUMBER."""
    parsed = urlparse(url)
    if parsed.scheme != "https" or parsed.netloc != "github.com":
        print(f"❌ Error: URL must start with https://github.com, got: {url}")
        sys.exit(1)

    # Allow trailing segments like /files or /commits that GitHub adds to PR tabs.
    parts = [p for p in parsed.path.split("/") if p]
    if len(parts) < 4 or parts[2] != "pull" or not parts[3].isdigit():
        print(f"❌ Error: Not a GitHub Pull Request URL: {url}")
        print("   Expected: https://github.com/OWNER/REPO/pull/NUMBER")
        sys.exit(1)

    return parts[0], parts[1], int(parts[3])


def fetch_diff(owner, repo, number):
    """Return (diff_text, was_truncated)."""
    url = f"https://github.com/{owner}/{repo}/pull/{number}.diff"
    response = requests.get(url, headers={"User-Agent": GITHUB_HEADERS["User-Agent"]}, timeout=30)
    if response.status_code != 200:
        print(f"❌ Error fetching diff: {response.status_code} {response.reason}")
        sys.exit(1)

    diff = response.text
    if len(diff) <= DIFF_LIMIT:
        return diff, False

    print(f"⚠️  Diff is {len(diff):,} characters, truncating to {DIFF_LIMIT:,}.")
    return diff[:DIFF_LIMIT] + "\n...[Diff Truncated]...", True


def github_get(url):
    response = requests.get(url, headers=GITHUB_HEADERS, timeout=30)
    if response.status_code == 200:
        return response.json()

    print(f"❌ GitHub API Error: {response.status_code} {response.reason}")
    # A 403/429 is usually the unauthenticated rate limit (60/hour), not a bug.
    if response.headers.get("X-RateLimit-Remaining") == "0":
        reset = datetime.fromtimestamp(int(response.headers.get("X-RateLimit-Reset", 0)))
        print(f"   Rate limit exhausted. It resets at {reset.strftime('%H:%M:%S')}.")
    else:
        try:
            print(f"   {response.json().get('message', '')}")
        except ValueError:
            pass
    sys.exit(1)


def fetch_pull_request(owner, repo, number):
    data = github_get(f"https://api.github.com/repos/{owner}/{repo}/pulls/{number}")
    return {
        "title": data["title"],
        "body": data["body"] or "[No description provided]",
        "author": data["user"]["login"],
        "created_at": data["created_at"],
        "url": data["html_url"],
    }


def fetch_comments(owner, repo, number):
    data = github_get(
        f"https://api.github.com/repos/{owner}/{repo}/issues/{number}/comments?per_page=100"
    )
    return [
        {
            # GitHub can return a null user for comments from deleted accounts.
            "username": (item["user"] or {}).get("login", "ghost"),
            "body": item["body"] or "[No message content]",
            "date": item["created_at"],
        }
        for item in data
    ]


def ask(prompt):
    print(prompt)
    try:
        return input("\n> ").strip()
    except EOFError:
        return ""


def get_student_understanding():
    print("\nBefore asking the LLM, form your own initial understanding.\n")
    interpretation = ask("In 2-4 sentences, what do you think this PR is changing, and why?")
    print()
    question = ask("What is one thing you don't understand yet?")
    print()
    return {"interpretation": interpretation, "question": question}


def escape_xml(text):
    """Escape untrusted text so a stray `</comment>` can't break the XML structure."""
    return escape(str(text), quote=True)


def diff_fence(diff):
    # A diff that edits Markdown may contain ``` itself. The outer fence must be
    # longer than any backtick run inside it, or the code block ends early.
    longest = max((len(run) for run in re.findall(r"`+", diff)), default=0)
    return "`" * max(3, longest + 1)


def build_user_prompt(pr, diff, truncated, comments, student):
    if comments:
        thread = "\n".join(
            f'<comment username="{escape_xml(c["username"])}" date="{escape_xml(c["date"])}">\n{escape_xml(c["body"])}\n</comment>'
            for c in comments
        )
    else:
        thread = "(No comments on this PR.)"

    fence = diff_fence(diff)
    truncation_note = (
        f"\nNOTE: The diff above was truncated at {DIFF_LIMIT:,} characters. "
        "Changes after that point are not visible.\n"
        if truncated
        else ""
    )

    return f"""Here is the Pull Request to analyze.

The PR metadata and description:

<pull-request>
<title>{escape_xml(pr["title"])}</title>
<author>{escape_xml(pr["author"])}</author>
<created-at>{escape_xml(pr["created_at"])}</created-at>
<url>{escape_xml(pr["url"])}</url>
<description>
{escape_xml(pr["body"])}
</description>
</pull-request>

The code changes (DIFF):

{fence}diff
{diff}
{fence}
{truncation_note}
The conversation history:

<thread>
{thread}
</thread>

The student's initial understanding, written before seeing any analysis:

<student-understanding>
<interpretation>
{escape_xml(student["interpretation"] or "[No answer given]")}
</interpretation>
<question>
{escape_xml(student["question"] or "[No answer given]")}
</question>
</student-understanding>

Analyze this PR and produce the Markdown report exactly as specified in your instructions."""


def generate(client, model, system_prompt, user_prompt):
    return client.chat.completions.create(
        model=model,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )


def generate_with_fallback(client, system_prompt, user_prompt):
    try:
        return generate(client, DEFAULT_MODEL, system_prompt, user_prompt)
    except APIError as e:
        reason = e.status_code if isinstance(e, APIStatusError) else type(e).__name__
        print(f"⚠️  {DEFAULT_MODEL} unavailable ({reason}), retrying with fallback model {FALLBACK_MODEL}...")
    try:
        return generate(client, FALLBACK_MODEL, system_prompt, user_prompt)
    except APIError as e:
        print(f"❌ Error: fallback model {FALLBACK_MODEL} also failed: {e}")
        sys.exit(1)


def main():
    print_header()

    if len(sys.argv) != 2:
        print("Usage: python pr-reader.py <github-pr-url>")
        sys.exit(1)
    owner, repo, number = parse_pr_url(sys.argv[1])
    api_key = load_api_key()

    with open(SYSTEM_PROMPT_PATH, "r", encoding="utf-8") as f:
        system_prompt = f.read()

    print(f"Fetching PR #{number} from {owner}/{repo}...")
    pr = fetch_pull_request(owner, repo, number)
    diff, truncated = fetch_diff(owner, repo, number)
    comments = fetch_comments(owner, repo, number)
    print(f'✅ "{pr["title"]}" by {pr["author"]}')
    print(f"✅ Diff: {len(diff):,} characters | Comments: {len(comments)}")

    student = get_student_understanding()
    user_prompt = build_user_prompt(pr, diff, truncated, comments, student)

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
        timeout=REQUEST_TIMEOUT_SECONDS,
        max_retries=0,  # we handle fallback ourselves
    )
    print("Asking your code-reading mentor...")
    response = generate_with_fallback(client, system_prompt, user_prompt)
    report = response.choices[0].message.content or ""

    if response.usage:
        print(
            f"Model: {response.model} | Tokens: "
            f"{response.usage.prompt_tokens} in, {response.usage.completion_tokens} out"
        )
    finish_reason = response.choices[0].finish_reason
    if not report.strip():
        print(f"❌ Empty response (finish reason: {finish_reason})")
        sys.exit(1)

    print("-" * 60)
    print(report)
    if finish_reason == "length":
        print("-" * 60)
        print(f"⚠️  The report hit the {MAX_TOKENS}-token limit and is cut off. Later sections may be missing.")


if __name__ == "__main__":
    main()
