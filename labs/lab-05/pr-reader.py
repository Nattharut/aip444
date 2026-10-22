#!/usr/bin/env python3
import json
import os
import re
import sys
from datetime import datetime
from html import escape
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI, APIError, APIStatusError

from tools import MAX_LINES, read_github_files

STUDENT_NAME = "Nattharut Natvongsakul"
STUDENT_ID = "184108231"

# Free instruction-tuned model first; paid version of the same model if the free
# one is rate-limited (429) or otherwise unavailable.
DEFAULT_MODEL = "google/gemma-4-31b-it:free"
FALLBACK_MODEL = "google/gemma-4-31b-it"

TEMPERATURE = 0.3
MAX_TOKENS = 4000
REQUEST_TIMEOUT_SECONDS = 180

# Every fetched file is re-sent with each later request, and each one can be
# ~15,000 tokens, so cap how many one analysis may read. This also keeps a run
# well under GitHub's 60 unauthenticated requests per hour.
MAX_FILES_TOTAL = 6

# Rounds of tool calls before the model is made to write the report with what
# it already has.
MAX_TOOL_ROUNDS = 3

# Arbitrary cap so one huge PR can't eat the model's whole context window.
# Characters, not tokens.
DIFF_LIMIT = 95_000

GITHUB_HEADERS = {
    "User-Agent": "AIP444-Lab-05",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2026-03-10",
}

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SYSTEM_PROMPT_PATH = os.path.join(SCRIPT_DIR, "SYSTEM_PROMPT.md")

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "read_github_files",
            "description": (
                "Read the full text of one or more files from a public GitHub repository. "
                "A diff shows only the changed lines and about three lines around them; use this tool "
                "when that is not enough to explain a change, for example to see where a function, "
                "variable, or constant used in the diff is defined or used, the rest of the function a "
                "small change sits in, or the other entries of a config file that changed. "
                "Do not use it when the diff already explains the change, for files the PR adds (the "
                "diff already shows every line), for lock, generated, minified, or binary files, or for "
                "paths you have not seen in the PR. "
                f"Files longer than {MAX_LINES:,} lines are cut to their first {MAX_LINES:,} lines. "
                f"At most {MAX_FILES_TOTAL} files can be read per PR, so request only the files you need, "
                "together in one call."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "files": {
                        "type": "array",
                        "description": "The files to read. Put every file you need in this one array.",
                        "items": {
                            "type": "object",
                            "properties": {
                                "owner": {
                                    "type": "string",
                                    "description": "Repository owner (user or organization), e.g. 'pallets' for github.com/pallets/flask.",
                                },
                                "repo": {
                                    "type": "string",
                                    "description": "Repository name, e.g. 'flask'.",
                                },
                                "path": {
                                    "type": "string",
                                    "description": (
                                        "File path inside the repository, exactly as in the diff header but without "
                                        "the a/ or b/ prefix, e.g. 'src/flask/app.py'."
                                    ),
                                },
                                "ref": {
                                    "type": "string",
                                    "description": (
                                        "Commit SHA, branch, or tag to read the file at. Use the PR's head SHA to "
                                        "see the file after the change, or its base SHA to see it before."
                                    ),
                                },
                            },
                            "required": ["owner", "repo", "path", "ref"],
                            "additionalProperties": False,
                        },
                    },
                },
                "required": ["files"],
                "additionalProperties": False,
            },
        },
    },
]


def print_header():
    run_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("AIP444 Fall 2026 - Lab 05")
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
    if len(parts) < 4 or parts[2] != "pull" or not parts[3].isdecimal() or not parts[3].isascii():
        print(f"❌ Error: Not a GitHub Pull Request URL: {url}")
        print("   Expected: https://github.com/OWNER/REPO/pull/NUMBER")
        sys.exit(1)

    return parts[0], parts[1], int(parts[3])


def http_get(url, headers):
    try:
        return requests.get(url, headers=headers, timeout=30)
    except requests.RequestException as err:
        print(f"❌ Network error fetching {url}")
        print(f"   {type(err).__name__}: {err}")
        sys.exit(1)


def fetch_diff(owner, repo, number):
    """Return (diff_text, was_truncated)."""
    url = f"https://github.com/{owner}/{repo}/pull/{number}.diff"
    response = http_get(url, {"User-Agent": GITHUB_HEADERS["User-Agent"]})
    if response.status_code != 200:
        print(f"❌ Error fetching diff: {response.status_code} {response.reason}")
        # GitHub refuses to generate very large diffs rather than sending one we
        # could truncate ourselves.
        if "too big" in response.text:
            print("   GitHub says this diff is too big to generate. Try a smaller PR.")
        sys.exit(1)

    diff = response.text
    if len(diff) <= DIFF_LIMIT:
        return diff, False

    print(f"⚠️  Diff is {len(diff):,} characters, truncating to {DIFF_LIMIT:,}.")
    return diff[:DIFF_LIMIT] + "\n...[Diff Truncated]...", True


def github_get(url):
    response = http_get(url, GITHUB_HEADERS)
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
        # The model reads files at these SHAs. A branch name like main may have
        # moved on since the PR (or the repo's default branch may be master).
        "base_ref": data["base"]["ref"],
        "base_sha": data["base"]["sha"],
        "head_sha": data["head"]["sha"],
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


def build_user_prompt(owner, repo, pr, diff, truncated, comments, student):
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
<repository>{escape_xml(owner)}/{escape_xml(repo)}</repository>
<base-branch>{escape_xml(pr["base_ref"])}</base-branch>
<base-sha>{pr["base_sha"]}</base-sha>
<head-sha>{pr["head_sha"]}</head-sha>
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

Decide whether the diff is enough or you need read_github_files (see "Reading Files from GitHub" in your instructions), then produce the Markdown report exactly as specified."""


def generate(client, model, messages, tool_choice):
    return client.chat.completions.create(
        model=model,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
        messages=messages,
        tools=TOOLS,
        tool_choice=tool_choice,
    )


def generate_with_fallback(client, model, messages, tool_choice):
    """Return (response, model_used). Once the fallback is used, later rounds skip the free model."""
    if model == DEFAULT_MODEL:
        try:
            return generate(client, DEFAULT_MODEL, messages, tool_choice), DEFAULT_MODEL
        except APIError as e:
            reason = e.status_code if isinstance(e, APIStatusError) else type(e).__name__
            print(f"⚠️  {DEFAULT_MODEL} unavailable ({reason}), retrying with fallback model {FALLBACK_MODEL}...")
    try:
        return generate(client, FALLBACK_MODEL, messages, tool_choice), FALLBACK_MODEL
    except APIError as e:
        print(f"❌ Error: fallback model {FALLBACK_MODEL} also failed: {e}")
        sys.exit(1)


def run_tool_call(tool_call, files_left):
    """Execute one tool call and return (result_for_the_llm, file_objects_fetched)."""
    name = tool_call.function.name
    arguments = tool_call.function.arguments or "{}"
    print(f"🔧 Tool call: {name}({arguments})")

    # Errors go back to the model as the tool result, with how to fix the call,
    # instead of crashing the program.
    if name != "read_github_files":
        return f"Error: there is no tool named {name!r}. The only tool is read_github_files.", []
    try:
        args = json.loads(arguments)
    except json.JSONDecodeError as err:
        return (
            f"Error: the arguments were not valid JSON ({err}). "
            'Send {"files": [{"owner": "...", "repo": "...", "path": "...", "ref": "..."}]}.'
        ), []
    files = args.get("files") if isinstance(args, dict) else None
    if not isinstance(files, list) or not files:
        return 'Error: "files" must be a non-empty array of {owner, repo, path, ref} objects.', []

    if files_left <= 0:
        print(f"   ⚠️  File limit ({MAX_FILES_TOTAL}) reached, nothing fetched")
        return (
            f"Error: the limit of {MAX_FILES_TOTAL} files for this PR has been reached. "
            "Write the report with the files you already have."
        ), []
    note = ""
    if len(files) > files_left:
        print(f"   ⚠️  {len(files)} files requested, only {files_left} left under the limit")
        note = (
            f"\n\nNote: only the first {files_left} of the {len(files)} requested files were read, "
            f"because one PR may read at most {MAX_FILES_TOTAL} files."
        )
        files = files[:files_left]
    return read_github_files(files) + note, files


def analyze(client, system_prompt, user_prompt):
    """Run the tool-calling loop and return (final_response, paths_requested_with_the_tool)."""
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]
    model = DEFAULT_MODEL
    files_left = MAX_FILES_TOTAL
    requested = []

    for round_number in range(MAX_TOOL_ROUNDS + 1):
        # After MAX_TOOL_ROUNDS rounds of fetching, "none" forces a written answer
        # instead of another request for files.
        last_round = round_number == MAX_TOOL_ROUNDS
        response, model = generate_with_fallback(client, model, messages, "none" if last_round else "auto")
        # OpenRouter can return HTTP 200 with an error object and no choices.
        if not response.choices:
            error = (response.model_extra or {}).get("error", "no choices in response")
            print(f"❌ OpenRouter returned no report: {error}")
            sys.exit(1)

        if response.usage:
            print(
                f"Model: {response.model} | Tokens: "
                f"{response.usage.prompt_tokens} in, {response.usage.completion_tokens} out"
            )
        message = response.choices[0].message
        if not message.tool_calls or last_round:
            return response, requested

        # Some models explain what they are about to fetch; show it while we wait.
        if message.content and message.content.strip():
            print(f"💬 {message.content.strip()}")
        # The assistant message with its tool_calls has to stay in the history,
        # or the tool results that follow have nothing to answer.
        messages.append(message)
        for tool_call in message.tool_calls:
            result, files = run_tool_call(tool_call, files_left)
            files_left -= len(files)
            requested += [f.get("path") for f in files if isinstance(f, dict)]
            messages.append({"role": "tool", "tool_call_id": tool_call.id, "content": result})


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
    user_prompt = build_user_prompt(owner, repo, pr, diff, truncated, comments, student)

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
        timeout=REQUEST_TIMEOUT_SECONDS,
        max_retries=0,  # we handle fallback ourselves
    )
    print("Asking your code-reading mentor...")
    response, requested = analyze(client, system_prompt, user_prompt)
    report = response.choices[0].message.content or ""
    finish_reason = response.choices[0].finish_reason
    if not report.strip():
        print(f"❌ Empty response (finish reason: {finish_reason})")
        sys.exit(1)

    print("-" * 60)
    print(report)
    if finish_reason == "length":
        print("-" * 60)
        print(f"⚠️  The report hit the {MAX_TOKENS}-token limit and is cut off. Later sections may be missing.")

    # The report's "Files read:" line is the model's own claim. Compare it with
    # what the program actually fetched, since a model can list files it never
    # requested.
    print("-" * 60)
    if requested:
        print(f"📚 Files requested with read_github_files: {', '.join(map(str, requested))}")
    else:
        print("📚 No files were requested with read_github_files.")
        if re.search(r"^[*_ ]*Files read:(?![*_`\s]*none)", report, re.MULTILINE | re.IGNORECASE):
            print(
                "⚠️  The report says it read files, but the tool was never called. "
                "Anything it says those files contain is unverified."
            )


if __name__ == "__main__":
    main()
