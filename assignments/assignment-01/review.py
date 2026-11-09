#!/usr/bin/env python3
"""AI code review: two reviewers in parallel, then a Lead Developer writes an HTML report.

Usage:
    python review.py                      # review staged changes (git diff --staged)
    python review.py --file bad_code.py   # review one file
    python review.py --debug --output report.html
"""
import argparse
import asyncio
import html
import json
import os
import random
import re
import subprocess
import sys
import time
from dataclasses import dataclass, field
from datetime import datetime

from dotenv import find_dotenv, load_dotenv
from openai import APIConnectionError, APIStatusError, APITimeoutError, AsyncOpenAI, RateLimitError
from pydantic import ValidationError

from schemas import ReviewResult
from tools import TOOLS, is_blocked, redact, resolve_inside, run_tool

REVIEWER_MODEL = "openai/gpt-oss-120b"
JUDGE_MODEL = "deepseek/deepseek-v4-flash"

# OpenRouter's default routing favours the cheapest provider. For the judge's
# ~5,000-token report that took 188s on one run; sorting by throughput took 16s
# for about the same cost. The reviewers stay on default routing: throughput
# made them ~10x faster but the whole review cost ~4x more.
REVIEWER_ROUTING = {}
JUDGE_ROUTING = {"sort": "throughput"}

REVIEWER_MAX_TOKENS = 8000
JUDGE_MAX_TOKENS = 16000
REQUEST_TIMEOUT_SECONDS = 180

# Rounds of tool calls before the reviewer must answer with what it has. Every
# tool result is re-sent on each later request, so rounds cost tokens fast.
MAX_TOOL_ROUNDS = 6

# 429s and 5xx from OpenRouter or the upstream provider. Waits are 2, 4, 8, 16s
# plus jitter, so two reviewers that hit the limit together don't retry in step.
MAX_RETRIES = 4

# Characters, not tokens. Roughly 15,000 tokens of code, which keeps a review
# cheap and leaves the model room to think.
MAX_INPUT_CHARS = 60_000

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROMPTS_DIR = os.path.join(SCRIPT_DIR, "prompts")

HUNK_HEADER = re.compile(r"^@@ -\d+(?:,\d+)? \+(\d+)(?:,\d+)? @@")


@dataclass
class Reviewer:
    name: str
    tag: str
    prompt_file: str
    temperature: float


REVIEWERS = [
    # Low: the same code should get the same security verdict every run.
    Reviewer("Security Auditor", "Security", "security.md", 0.1),
    # Low-medium: some room for refactoring ideas while staying on the code.
    Reviewer("Maintainability Critic", "Maintainability", "maintainability.md", 0.4),
]
JUDGE_TEMPERATURE = 0.3


class ReviewError(Exception):
    """A failure with a message meant for the user."""


@dataclass
class Usage:
    prompt_tokens: int = 0
    completion_tokens: int = 0
    cost: float = 0.0
    requests: int = 0

    def add(self, usage):
        if usage is None:
            return
        self.requests += 1
        self.prompt_tokens += usage.prompt_tokens or 0
        self.completion_tokens += usage.completion_tokens or 0
        # OpenRouter adds the dollar cost of each request to usage.
        self.cost += float((usage.model_extra or {}).get("cost") or 0)


@dataclass
class Logger:
    debug: bool
    started: float = field(default_factory=time.monotonic)

    def log(self, tag, message):
        """Debug-only detail. Everything goes to stderr; stdout is for the final result."""
        if self.debug:
            elapsed = time.monotonic() - self.started
            print(f"[{elapsed:6.1f}s] [{tag}] {message}", file=sys.stderr, flush=True)

    def status(self, message):
        """Progress shown with or without --debug."""
        if self.debug:
            self.log("Main", message)
        else:
            print(message, file=sys.stderr, flush=True)


def fail(message):
    print(f"Error: {message}", file=sys.stderr)
    sys.exit(1)


def preview(text, max_lines=15):
    lines = text.splitlines()
    shown = "\n".join(f"    {line}" for line in lines[:max_lines])
    if len(lines) > max_lines:
        shown += f"\n    ... ({len(lines) - max_lines} more lines)"
    return shown


def git(*args, cwd=None):
    try:
        return subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)
    except FileNotFoundError:
        fail("git is not installed or not on PATH. Install git, or review a single file with --file.")


def git_root(directory):
    result = git("rev-parse", "--show-toplevel", cwd=directory)
    return os.path.realpath(result.stdout.strip()) if result.returncode == 0 else None


def number_diff(diff):
    """Prefix each hunk line with its line number in the new file, so findings cite real lines."""
    out = []
    new_line = None
    for line in diff.splitlines():
        header = HUNK_HEADER.match(line)
        if header:
            new_line = int(header.group(1))
            out.append(line)
        elif line.startswith("diff --git"):
            new_line = None
            out.append(line)
        elif new_line is None or line.startswith("\\"):
            # File headers, "Binary files differ", "\ No newline at end of file".
            out.append(line)
        elif line.startswith("-"):
            out.append(f"{'':>5} {line}")
        else:
            # "+" lines and context lines (" ", or "" when trailing space was stripped).
            out.append(f"{new_line:>5} {line}")
            new_line += 1
    return "\n".join(out)


def truncate_input(text):
    if len(text) <= MAX_INPUT_CHARS:
        return text, False
    cut = text.rfind("\n", 0, MAX_INPUT_CHARS)
    return text[:cut] + f"\n[Input truncated: showing the first {cut:,} of {len(text):,} characters]", True


def load_git_input(log):
    root = git_root(os.getcwd())
    if root is None:
        fail("not inside a git repository. Run review from a repository with staged changes, or use --file.")
    result = git("diff", "--staged", "--no-color", "--no-ext-diff", cwd=root)
    if result.returncode != 0:
        fail(f"git diff --staged failed: {result.stderr.strip()}")
    diff = result.stdout
    if not diff.strip():
        print(
            "Nothing to review: there are no staged changes. Stage files with `git add <file>`, "
            "or review a single file with --file <path>.",
            file=sys.stderr,
        )
        sys.exit(0)

    files = re.findall(r"^diff --git a/(.+?) b/", diff, re.MULTILINE)
    log.log("Main", f"Git mode: {len(files)} staged file(s), {len(diff):,} characters of diff: {', '.join(files)}")
    body, truncated = truncate_input(redact(number_diff(diff)))
    if truncated:
        log.status(f"Warning: the diff is over {MAX_INPUT_CHARS:,} characters; reviewers see only the first part.")
    return {
        "root": root,
        "mode": "diff",
        "target": f"{len(files)} staged file(s): {', '.join(files)}",
        "prompt": f'<review-input mode="diff">\n{body}\n</review-input>',
    }


def load_file_input(file_arg, log):
    path = os.path.realpath(file_arg)
    if not os.path.exists(path):
        fail(f"file not found: {file_arg}")
    if not os.path.isfile(path):
        fail(f"not a regular file: {file_arg}")
    try:
        with open(path, "rb") as f:
            raw = f.read()
    except OSError as err:
        fail(f"cannot read {file_arg}: {err.strerror}")
    if b"\x00" in raw[:8000]:
        fail(f"{file_arg} looks like a binary file; only text files can be reviewed.")
    text = raw.decode("utf-8", errors="replace")
    if not text.strip():
        print(f"Nothing to review: {file_arg} is empty.", file=sys.stderr)
        sys.exit(0)

    # Tools search the file's repository, so a reviewer can follow imports and callers.
    root = git_root(os.path.dirname(path)) or os.path.dirname(path)
    relative = os.path.relpath(path, root)
    if is_blocked(relative):
        fail(f"{file_arg} is a secret or dependency file; it will not be sent to the LLM.")

    lines = text.splitlines()
    log.log("Main", f"File mode: {relative} ({len(lines)} lines), tools rooted at {root}")
    numbered = "\n".join(f"{n:>5}| {line}" for n, line in enumerate(lines, start=1))
    body, truncated = truncate_input(numbered)
    if truncated:
        log.status(f"Warning: {relative} is over {MAX_INPUT_CHARS:,} characters; reviewers see only the first part.")
    return {
        "root": root,
        "mode": "file",
        "target": relative,
        "prompt": f'<review-input mode="file" path="{relative}">\n{redact(body)}\n</review-input>',
    }


def load_prompt(name):
    with open(os.path.join(PROMPTS_DIR, name), "r", encoding="utf-8") as f:
        return f.read()


async def create(client, log, tag, usage, **kwargs):
    """chat.completions.create with exponential backoff on rate limits and server errors."""
    for attempt in range(MAX_RETRIES + 1):
        try:
            response = await client.chat.completions.create(**kwargs)
        except (RateLimitError, APIConnectionError, APITimeoutError, APIStatusError) as err:
            status = getattr(err, "status_code", None)
            retryable = status is None or status == 429 or status >= 500
            if not retryable:
                raise ReviewError(f"{tag}: OpenRouter rejected the request (HTTP {status}): {err.message}") from err
            reason = f"HTTP {status}" if status else type(err).__name__
        else:
            usage.add(response.usage)
            if response.choices:
                if response.usage:
                    log.log(
                        tag,
                        f"Model {response.model}: {response.usage.prompt_tokens} tokens in, "
                        f"{response.usage.completion_tokens} out",
                    )
                return response
            # OpenRouter can return HTTP 200 with an error object and no choices,
            # usually an upstream provider failing.
            reason = str((response.model_extra or {}).get("error", "no choices in response"))

        if attempt == MAX_RETRIES:
            raise ReviewError(
                f"{tag}: gave up after {MAX_RETRIES + 1} attempts ({reason}). "
                "OpenRouter may be rate-limiting this key or the model may be down; wait a minute and try again."
            )
        delay = 2 ** (attempt + 1) + random.uniform(0, 1)
        log.log(tag, f"Request failed ({reason}); retrying in {delay:.1f}s (attempt {attempt + 2}/{MAX_RETRIES + 1})")
        await asyncio.sleep(delay)


def parse_findings(content):
    text = (content or "").strip()
    # Some models wrap JSON in a Markdown fence despite the instructions.
    fenced = re.match(r"^```(?:json)?\s*(.*?)\s*```$", text, re.DOTALL)
    if fenced:
        text = fenced.group(1)
    return ReviewResult.model_validate_json(text).findings


async def run_reviewer(client, reviewer, review_input, common_prompt, log, usage):
    tag = reviewer.tag
    log.status(f"{reviewer.name} started")
    messages = [
        {"role": "system", "content": load_prompt(reviewer.prompt_file) + "\n\n" + common_prompt},
        {"role": "user", "content": review_input["prompt"]},
    ]
    request = dict(
        model=REVIEWER_MODEL,
        temperature=reviewer.temperature,
        max_tokens=REVIEWER_MAX_TOKENS,
        # require_parameters: route only to providers that support every parameter
        # sent (tools, response_format), not one that silently ignores them.
        extra_body={"provider": REVIEWER_ROUTING | {"require_parameters": True}, "usage": {"include": True}},
    )

    # Phase A: investigate. No response_format here: providers enforce the schema
    # with constrained decoding, which makes a tool call impossible, so a model
    # given both answers {"findings": []} without ever looking anything up.
    for round_number in range(MAX_TOOL_ROUNDS):
        response = await create(client, log, tag, usage, messages=messages, tools=TOOLS, tool_choice="auto", **request)
        message = response.choices[0].message
        if not message.tool_calls:
            log.log(tag, f"Done investigating after {round_number} tool round(s)")
            messages.append({"role": "assistant", "content": message.content or ""})
            break
        if message.content and message.content.strip():
            log.log(tag, f"Says: {message.content.strip()[:300]}")
        # The assistant turn with its tool_calls must stay in the history, or
        # the tool results that follow answer nothing.
        messages.append({
            "role": "assistant",
            "content": message.content or "",
            "tool_calls": [call.model_dump() for call in message.tool_calls],
        })
        for call in message.tool_calls:
            name = call.function.name
            arguments = call.function.arguments or "{}"
            log.log(tag, f"Calling {name}({arguments})")
            try:
                args = json.loads(arguments)
                if not isinstance(args, dict):
                    raise ValueError
            except ValueError:
                result, summary = f"Error: arguments must be a JSON object, got {arguments!r}.", "bad arguments"
            else:
                # In a thread, so a slow ripgrep doesn't stall the other reviewer.
                result, summary = await asyncio.to_thread(run_tool, review_input["root"], name, args)
            log.log("Tool", f"{name} -> {summary}\n{preview(result)}")
            messages.append({"role": "tool", "tool_call_id": call.id, "content": result})
    else:
        log.log(tag, f"Tool round limit ({MAX_TOOL_ROUNDS}) reached; asking for findings")

    # Phase B: the structured answer, with the schema enforced. tools is left out
    # entirely: with tools present, even with tool_choice="none", gpt-oss-120b and
    # deepseek-v4-flash both returned empty content in testing.
    messages.append({
        "role": "user",
        "content": "Investigation is over. Return your final findings as the JSON object, following the "
                   "Grounding rules: only issues in your area of focus, each with an exact evidence line.",
    })
    response_format = {
        "type": "json_schema",
        "json_schema": {"name": "review_result", "strict": True, "schema": ReviewResult.model_json_schema()},
    }
    for attempt in range(2):
        response = await create(
            client, log, tag, usage,
            messages=messages, response_format=response_format, **request,
        )
        content = response.choices[0].message.content
        try:
            findings = parse_findings(content)
        except ValidationError as err:
            finish = response.choices[0].finish_reason
            log.log(tag, f"Invalid JSON (finish reason {finish}): {err.errors()[0]['msg']}\n{preview(content or '')}")
            if attempt == 1:
                raise ReviewError(f"{reviewer.name} did not return valid JSON (finish reason: {finish}).") from err
            continue
        log.status(f"{reviewer.name} finished: {len(findings)} finding(s)")
        return findings


def verify_evidence(finding, root, log, tag):
    """Check the quoted line exists in the file, and fix the line number if it's nearby but off."""
    record = finding.model_dump()
    record["evidence_verified"] = False
    evidence = finding.evidence.strip()
    full = resolve_inside(root, finding.path)
    if not evidence or full is None or is_blocked(os.path.relpath(full, root)) or not os.path.isfile(full):
        log.log(tag, f"Unverified: {finding.path}:{finding.line} (file not readable)")
        return record
    with open(full, "r", encoding="utf-8", errors="replace") as f:
        lines = f.read().splitlines()

    exact = [n for n, line in enumerate(lines, start=1) if line.strip() == evidence]
    # Models sometimes quote part of a line, or a line plus a trailing comment.
    # The length floor stops "}" or "return x" from matching anywhere.
    partial = [
        n for n, line in enumerate(lines, start=1)
        if len(evidence) >= 8 and evidence in line or len(line.strip()) >= 8 and line.strip() in evidence
    ]
    candidates = exact or partial
    if not candidates:
        log.log(tag, f"Unverified: evidence not found in {finding.path}: {evidence[:80]!r}")
        return record
    record["evidence_verified"] = True
    closest = min(candidates, key=lambda n: abs(n - finding.line))
    if closest != finding.line:
        log.log(tag, f"Line corrected: {finding.path}:{finding.line} -> {closest} (where the evidence is)")
        record["line"] = closest
    return record


def secret_values(results):
    """String literals quoted as evidence in secrets findings, e.g. the key in api_key = "sk-...".

    The judge is told to mask secrets but doesn't always, and the report is a
    file people share, so masking is done here instead of trusted to the model.
    """
    values = set()
    for _, findings in results:
        if isinstance(findings, Exception):
            continue
        for finding in findings:
            if "secret" in finding["category"].lower() or "credential" in finding["category"].lower():
                evidence = finding["evidence"]
                values.update(re.findall(r"[\"']([^\"']{8,})[\"']", evidence))
                # Unquoted assignments, as in .env files or docs: DB_PASS=admin123
                values.update(re.findall(r"[=:]\s*([^\s\"'`,;]{6,})", evidence))
    return values


def mask_secrets(text, secrets):
    for value in secrets:
        masked = value[:4] + "..."
        text = text.replace(value, masked).replace(html.escape(value), masked)
    return text


def build_judge_prompt(review_input, results):
    parts = [
        "<review-meta>",
        f"mode: {'staged git diff' if review_input['mode'] == 'diff' else 'single file'}",
        f"target: {review_input['target']}",
        f"date: {datetime.now().strftime('%d %B %Y, %H:%M')}",
        "</review-meta>",
        "",
        review_input["prompt"],
        "",
    ]
    for reviewer, findings in results:
        if isinstance(findings, Exception):
            parts.append(f'<reviewer name="{reviewer.name}" status="failed">{findings}</reviewer>')
        else:
            parts.append(f'<reviewer name="{reviewer.name}">\n{json.dumps(findings, indent=2)}\n</reviewer>')
    if any(isinstance(findings, Exception) for _, findings in results):
        parts.append("\nOne reviewer failed. Say so in the verdict banner, and review only the findings you have.")
    return "\n".join(parts)


def extract_html(content):
    text = (content or "").strip()
    start = re.search(r"<!DOCTYPE html|<html", text, re.IGNORECASE)
    end = text.lower().rfind("</html>")
    if not start:
        return None
    return text[start.start(): end + len("</html>") if end != -1 else len(text)]


async def run_judge(client, review_input, results, log, usage):
    log.status("Lead Developer started")
    secrets = secret_values(results)
    prompt = mask_secrets(build_judge_prompt(review_input, results), secrets)
    if secrets:
        log.log("Judge", f"Masked {len(secrets)} secret value(s) in the judge prompt and report")
    log.log("Judge", f"Prompt: {len(prompt):,} characters")
    response = await create(
        client, log, "Judge", usage,
        model=JUDGE_MODEL,
        temperature=JUDGE_TEMPERATURE,
        max_tokens=JUDGE_MAX_TOKENS,
        messages=[
            {"role": "system", "content": load_prompt("judge.md")},
            {"role": "user", "content": prompt},
        ],
        extra_body={"provider": JUDGE_ROUTING, "usage": {"include": True}},
    )
    choice = response.choices[0]
    report = extract_html(choice.message.content)
    if report is None:
        log.log("Judge", f"Response without HTML:\n{preview(choice.message.content or '')}")
        raise ReviewError(f"the Lead Developer did not return an HTML document (finish reason: {choice.finish_reason}).")
    if choice.finish_reason == "length":
        log.status(f"Warning: the report hit the {JUDGE_MAX_TOKENS}-token limit and may be cut off.")
    log.status("Lead Developer finished")
    return mask_secrets(report, secrets)


async def review(args, log):
    # Before loading the input: redact() needs the key to scrub it from what is sent.
    # find_dotenv() searches up from this script, not the cwd, so reviewing another
    # repository doesn't pick up that repository's .env.
    load_dotenv(find_dotenv())
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        fail("OPENROUTER_API_KEY is not set. Add it to a .env file in the repository root (it is gitignored).")

    review_input = load_file_input(args.file, log) if args.file else load_git_input(log)

    client = AsyncOpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
        timeout=REQUEST_TIMEOUT_SECONDS,
        max_retries=0,  # create() retries with its own backoff and logging
    )
    usage = Usage()
    common_prompt = load_prompt("reviewer_common.md")

    log.status(f"Reviewing {review_input['target']} with {len(REVIEWERS)} reviewers in parallel ({REVIEWER_MODEL})...")
    raw = await asyncio.gather(
        *(run_reviewer(client, r, review_input, common_prompt, log, usage) for r in REVIEWERS),
        return_exceptions=True,
    )

    results = []
    for reviewer, outcome in zip(REVIEWERS, raw):
        if isinstance(outcome, Exception):
            if not isinstance(outcome, ReviewError):
                raise outcome
            log.status(f"Warning: {outcome}")
            results.append((reviewer, outcome))
            continue
        records = [verify_evidence(f, review_input["root"], log, reviewer.tag) for f in outcome]
        log.log(reviewer.tag, f"Raw findings ({len(records)}):\n{json.dumps(records, indent=2)}")
        results.append((reviewer, records))
    if all(isinstance(findings, Exception) for _, findings in results):
        fail("both reviewers failed, so there is nothing to report.")

    report = await run_judge(client, review_input, results, log, usage)
    await client.close()

    output = args.output or datetime.now().strftime("review-%d-%m-%Y-%H-%M-%S.html")
    try:
        with open(output, "w", encoding="utf-8") as f:
            f.write(report)
    except OSError as err:
        fail(f"cannot write the report to {output}: {err.strerror}")

    log.status(
        f"{usage.requests} requests, {usage.prompt_tokens:,} tokens in, {usage.completion_tokens:,} out, "
        f"cost ${usage.cost:.4f}"
    )
    return output


def main():
    parser = argparse.ArgumentParser(
        prog="review",
        description="AI code review of staged git changes (default) or one file, written to an HTML report.",
    )
    parser.add_argument("--file", help="review this file instead of the staged git diff")
    parser.add_argument("--output", help="HTML report path (default: review-DD-MM-YYYY-HH-MM-SS.html)")
    parser.add_argument("--debug", action="store_true", help="log every step, tool call, and raw finding to stderr")
    args = parser.parse_args()

    log = Logger(debug=args.debug)
    try:
        output = asyncio.run(review(args, log))
    except ReviewError as err:
        fail(str(err))
    except KeyboardInterrupt:
        print("\nCancelled.", file=sys.stderr)
        sys.exit(130)
    print(f"Report saved to {output}")


if __name__ == "__main__":
    main()
