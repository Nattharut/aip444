import hashlib
import os
import re
from urllib.parse import quote

import requests

# Files longer than this are cut to their first MAX_LINES lines. The top of a
# file (imports, constants, class and function definitions) usually explains
# the most, and 1,000 lines of code is roughly 10,000-15,000 tokens.
MAX_LINES = 1000

# A minified bundle can be a single enormous line, which MAX_LINES wouldn't catch.
MAX_CHARS = 60_000

REQUEST_TIMEOUT_SECONDS = 30
USER_AGENT = "AIP444-Lab-05"

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CACHE_DIR = os.path.join(SCRIPT_DIR, ".cache")

FULL_SHA = re.compile(r"[0-9a-f]{40}")


def raw_url(owner, repo, path, ref):
    # raw.githubusercontent.com resolves branch names (even ones with slashes,
    # like release/1.99), tags, and commit SHAs as-is. Rewriting a branch to
    # refs/heads/{ref} would break tags and SHAs, so ref is passed through.
    return (
        f"https://raw.githubusercontent.com/{quote(owner)}/{quote(repo)}/"
        f"{quote(ref, safe='/')}/{quote(path, safe='/')}"
    )


def cache_path(url):
    # Name the file by a hash of the URL instead of mirroring owner/repo/path on
    # disk: path comes from the LLM, and a "../" in it must not be able to write
    # outside .cache/.
    return os.path.join(CACHE_DIR, hashlib.sha256(url.encode()).hexdigest() + ".txt")


def fetch_file(owner, repo, path, ref):
    """Return (text, from_cache, error). error is None on success, else a message for the LLM."""
    url = raw_url(owner, repo, path, ref)
    # Only a commit SHA always points at the same content. A branch moves, so
    # caching main would serve a stale file on the next run.
    cacheable = FULL_SHA.fullmatch(ref) is not None
    cached = cache_path(url)
    if cacheable and os.path.exists(cached):
        with open(cached, "r", encoding="utf-8") as f:
            return f.read(), True, None

    try:
        response = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=REQUEST_TIMEOUT_SECONDS)
    except requests.RequestException as err:
        return None, False, (
            f"could not reach GitHub ({type(err).__name__}). Do not retry this file; "
            "explain the change from the diff and say the file could not be read."
        )

    if response.status_code == 404:
        # raw.githubusercontent.com returns the same 404 for a wrong owner, repo,
        # ref, or path, so the message lists every cause.
        return None, False, (
            f"not found (404). The owner, repo, or path is wrong, or the file does not exist at ref {ref} "
            "(a file the PR adds is not in the base commit, and a file it deletes is not in the head commit). "
            "Use the path exactly as in the diff header, without the a/ or b/ prefix. Do not guess other paths."
        )
    if response.status_code in (403, 429):
        return None, False, (
            f"GitHub refused the request (HTTP {response.status_code}), most likely its rate limit of "
            "60 requests per hour. Do not request more files; write the report with what you already have."
        )
    if response.status_code != 200:
        return None, False, f"GitHub returned HTTP {response.status_code} {response.reason}. Do not retry this file."

    if b"\x00" in response.content[:8000]:
        return None, False, "this is a binary file (for example an image or archive), so it has no text to show."

    text = response.text
    if cacheable:
        os.makedirs(CACHE_DIR, exist_ok=True)
        with open(cached, "w", encoding="utf-8") as f:
            f.write(text)
    return text, False, None


def truncate(text):
    """Return (text, line_count, note). note is None unless the text was cut."""
    lines = text.splitlines()
    note = None
    if len(lines) > MAX_LINES:
        text = "\n".join(lines[:MAX_LINES])
        note = f"[File truncated: showing first {MAX_LINES:,} of {len(lines):,} lines]"
    if len(text) > MAX_CHARS:
        text = text[:MAX_CHARS]
        note = f"[File truncated: showing first {MAX_CHARS:,} characters of a {len(lines):,}-line file]"
    return text, len(lines), note


def code_fence(text):
    # A Markdown file may contain ``` itself. The outer fence must be longer than
    # any backtick run inside it, or the code block ends early.
    longest = max((len(run) for run in re.findall(r"`+", text)), default=0)
    return "`" * max(3, longest + 1)


def read_one_file(file):
    """Fetch one file object and return its Markdown section."""
    if not isinstance(file, dict) or not all(
        isinstance(file.get(key), str) and file[key].strip() for key in ("owner", "repo", "path")
    ):
        print(f"   ⚠️  Invalid file object: {file!r}")
        return (
            f"## Invalid file request\n\nError: {file!r} is not a valid file object. "
            'Each file needs non-empty "owner", "repo", and "path" strings, plus "ref".'
        )

    owner = file["owner"].strip()
    repo = file["repo"].strip()
    path = file["path"].strip().lstrip("/")
    ref = (file.get("ref") or "main").strip()
    label = f"{owner}/{repo}/{path} @ {ref}"

    text, from_cache, error = fetch_file(owner, repo, path, ref)
    if error:
        print(f"   ❌ {label}: {error.split('.')[0]}")
        return f"## {label}\n\nError: {error}"

    text, line_count, note = truncate(text)
    source = "cache" if from_cache else "GitHub"
    print(f"   📄 {label}: {line_count:,} lines from {source}{' (truncated)' if note else ''}")
    fence = code_fence(text)
    section = f"## {label}\n\n{fence}\n{text}\n{fence}"
    if note:
        section += f"\n{note}"
    return section


def read_github_files(files):
    """Fetch files from raw.githubusercontent.com and return them as one Markdown string.

    files is a list of {"owner", "repo", "path", "ref"} dicts, where ref is a
    branch, tag, or commit SHA and defaults to "main". Each file gets its own
    "## owner/repo/path @ ref" section. A file that fails gets an "Error:" line
    in its section instead of stopping the others, so the LLM still receives
    every file that worked.
    """
    if not isinstance(files, list) or not files:
        return 'Error: "files" must be a non-empty array of {owner, repo, path, ref} objects.'
    return "\n\n".join(read_one_file(file) for file in files)
