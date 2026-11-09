import os
import shutil
import subprocess
import sys

# One read_file call returns at most this many lines. A reviewer that needs more
# asks for the next range, so a 20,000-line lock file never lands in one prompt.
MAX_LINES = 400

# A minified bundle can be a single enormous line, which MAX_LINES wouldn't catch.
MAX_CHARS = 40_000

MAX_MATCH_LINES = 100
MAX_MATCH_CHARS = 15_000
RG_TIMEOUT_SECONDS = 20

# Never searched or read, whatever the model asks for. .env holds the
# OpenRouter key, and anything a tool returns is sent to the LLM provider and
# can end up quoted in the HTML report.
BLOCKED_GLOBS = [".env", ".env.*", ".git", ".venv", "venv", "node_modules", "*.lock", "package-lock.json"]

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": (
                "Read lines of a file in the repository being reviewed. Each returned line is prefixed with its "
                "1-based line number and '| ', which is not part of the file. Use it to see code outside the "
                "diff: imports, the rest of a function, a class definition, or a config file. "
                f"One call returns at most {MAX_LINES} lines; the result says how to request the next range. "
                "Secret files (.env), .git, and dependency folders cannot be read."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "file_path": {
                        "type": "string",
                        "description": "Path relative to the repository root, e.g. 'src/app.py'. No a/ or b/ diff prefix.",
                    },
                    "start_line": {
                        "type": "integer",
                        "description": "First line to return (1-based, inclusive). Omit to start at line 1.",
                    },
                    "end_line": {
                        "type": "integer",
                        "description": "Last line to return (inclusive). Omit to read to the end, up to the line limit.",
                    },
                },
                "required": ["file_path"],
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "ripgrep",
            "description": (
                "Search every file in the repository for a regular expression (ripgrep / Rust regex syntax) and "
                "return matching lines as 'path:line:text'. Use it to find where a function or variable is "
                "defined or called, whether an import is used, or whether a risky pattern appears elsewhere. "
                "Escape regex metacharacters to match them literally, e.g. 'calculate_total\\(' . "
                f"At most {MAX_MATCH_LINES} matching lines are returned."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "search_pattern": {
                        "type": "string",
                        "description": "Regular expression to search for, e.g. 'def calculate_total' or 'api_key\\s*='.",
                    },
                },
                "required": ["search_pattern"],
                "additionalProperties": False,
            },
        },
    },
]

TOOL_NAMES = [tool["function"]["name"] for tool in TOOLS]


def redact(text):
    # Last line of defence: if the key reaches a tool result anyway (say, pasted
    # into a source file), it is never sent on to the model.
    key = os.getenv("OPENROUTER_API_KEY")
    return text.replace(key, "[REDACTED]") if key else text


def is_blocked(relative_path):
    parts = relative_path.replace(os.sep, "/").split("/")
    for part in parts:
        if part in (".git", ".venv", "venv", "node_modules"):
            return True
    name = parts[-1]
    return name == ".env" or name.startswith(".env.")


def resolve_inside(root, file_path):
    """Return the absolute path, or None if it points outside root (via ../ or a symlink)."""
    full = os.path.realpath(os.path.join(root, file_path))
    return full if full == root or full.startswith(root + os.sep) else None


def read_file(root, file_path, start_line=None, end_line=None):
    """Return (text_for_the_llm, short_summary_for_the_log)."""
    if not isinstance(file_path, str) or not file_path.strip():
        return "Error: file_path must be a non-empty string.", "invalid file_path"
    full = resolve_inside(root, file_path)
    if full is None:
        return f"Error: {file_path!r} is outside the repository. Only files inside it can be read.", "outside repo"
    relative = os.path.relpath(full, root)
    if is_blocked(relative):
        return f"Error: {relative} is a secret or dependency file and cannot be read.", "blocked"
    if not os.path.isfile(full):
        return (
            f"Error: {relative} does not exist or is not a file. Use paths exactly as shown in the input, "
            "or find the right one with ripgrep. Do not guess."
        ), "not found"

    with open(full, "rb") as f:
        raw = f.read()
    if b"\x00" in raw[:8000]:
        return f"Error: {relative} is a binary file and has no text to show.", "binary"

    lines = raw.decode("utf-8", errors="replace").splitlines()
    total = len(lines)
    if total == 0:
        return f"{relative} is empty.", "empty file"

    # Models sometimes send line numbers as strings ("10").
    try:
        start_line = int(start_line) if start_line is not None else None
        end_line = int(end_line) if end_line is not None else None
    except (TypeError, ValueError):
        return "Error: start_line and end_line must be integers.", "bad range"

    start = max(1, start_line or 1)
    if start > total:
        return f"Error: start_line {start} is past the end of {relative}, which has {total} lines.", "bad range"
    end = min(total, end_line or total, start + MAX_LINES - 1)
    if end < start:
        return f"Error: end_line {end_line} is before start_line {start}.", "bad range"

    body = "\n".join(f"{n:>5}| {lines[n - 1]}" for n in range(start, end + 1))
    if len(body) > MAX_CHARS:
        body = body[:MAX_CHARS]
        # The cut can land mid-line; find the last line that survived whole.
        end = start + body.count("\n") - 1
        body = body[: body.rfind("\n")]
    header = f"{relative} (lines {start}-{end} of {total})"
    if end < total:
        header += f". More lines follow: call read_file with start_line={end + 1} to continue."
    return redact(f"{header}\n{body}"), f"{end - start + 1} lines of {relative} ({start}-{end} of {total})"


def find_rg():
    # The ripgrep PyPI package puts rg next to the venv's python, which may not
    # be on PATH when review.py is run as .venv/bin/python review.py.
    local = os.path.join(os.path.dirname(sys.executable), "rg")
    return local if os.access(local, os.X_OK) else shutil.which("rg")


def ripgrep(root, search_pattern):
    """Return (text_for_the_llm, short_summary_for_the_log)."""
    if not isinstance(search_pattern, str) or not search_pattern:
        return "Error: search_pattern must be a non-empty string.", "invalid pattern"
    rg = find_rg()
    if rg is None:
        return "Error: ripgrep is not installed, so searching is unavailable. Review with what you have.", "rg missing"

    command = [
        rg, "--line-number", "--no-heading", "--color=never",
        "--max-columns=300", "--max-columns-preview", "--max-count=20", "--max-filesize=1M",
    ]
    for glob in BLOCKED_GLOBS:
        command.append(f"--glob=!{glob}")
    # -e so a pattern starting with '-' isn't read as a flag; '.' so rg never
    # decides to search stdin instead of the repository.
    command += ["-e", search_pattern, "."]
    try:
        result = subprocess.run(command, cwd=root, capture_output=True, text=True, timeout=RG_TIMEOUT_SECONDS)
    except subprocess.TimeoutExpired:
        return f"Error: the search took longer than {RG_TIMEOUT_SECONDS}s. Use a more specific pattern.", "timeout"

    if result.returncode == 1:
        return f"No matches for {search_pattern!r}.", "0 matches"
    if result.returncode != 0:
        message = result.stderr.strip().splitlines()[-1] if result.stderr.strip() else "unknown error"
        return (
            f"Error: invalid search ({message}). Patterns are regular expressions; escape characters "
            "like ( ) [ ] . * + ? with a backslash to match them literally."
        ), "rg error"

    matches = [line.removeprefix("./") for line in result.stdout.splitlines()]
    shown = matches[:MAX_MATCH_LINES]
    text = "\n".join(shown)
    if len(text) > MAX_MATCH_CHARS:
        text = text[: text.rfind("\n", 0, MAX_MATCH_CHARS)]
        shown = text.splitlines()
    if len(shown) < len(matches):
        text += f"\n[Showing {len(shown)} of {len(matches)} matching lines. Use a more specific pattern to see the rest.]"
    files = len({m.split(":", 1)[0] for m in matches})
    return redact(text), f"{len(matches)} matches in {files} files"


def run_tool(root, name, args):
    """Dispatch one tool call. args is the already-parsed JSON object."""
    # gpt-oss-120b repeatedly sent ripgrep {"path": ...}; a generic "must be a
    # non-empty string" error didn't stop it, naming the wrong key does.
    schema = next((t["function"]["parameters"] for t in TOOLS if t["function"]["name"] == name), None)
    if schema is not None:
        unknown = sorted(set(args) - set(schema["properties"]))
        if unknown:
            return (
                f"Error: {name} has no argument named {', '.join(unknown)}. "
                f"Its arguments are: {', '.join(schema['properties'])} (required: {', '.join(schema['required'])})."
            ), f"unknown argument {', '.join(unknown)}"
    if name == "read_file":
        return read_file(root, args.get("file_path"), args.get("start_line"), args.get("end_line"))
    if name == "ripgrep":
        return ripgrep(root, args.get("search_pattern"))
    return (
        f"Error: there is no tool named {name!r}. The only tools are {', '.join(TOOL_NAMES)}.",
        "unknown tool",
    )
