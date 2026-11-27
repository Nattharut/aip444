#!/usr/bin/env python3
import argparse
import asyncio
import json
import os
import re
import sys
from collections import Counter
from datetime import date, datetime
from urllib.parse import urlparse

# The SDK leaves the pydantic error out of a rejected tool call unless this is
# off, so the model would only hear "Invalid JSON input for tool ..." and not
# which field (say transparency_score=7) to fix. It is read once, at import.
os.environ.setdefault("OPENAI_AGENTS_DONT_LOG_TOOL_DATA", "0")

from agents import (
    Agent,
    AgentsException,
    MaxTurnsExceeded,
    OpenAIChatCompletionsModel,
    RunHooks,
    Runner,
    set_default_openai_api,
    set_default_openai_client,
    set_tracing_disabled,
)
from dotenv import find_dotenv, load_dotenv
from openai import APIError, AsyncOpenAI

from tools import RunInfo, assess_credibility, read_url, save_report, web_search

MODEL = "deepseek/deepseek-v4.1-flash-1017"

# Guardrail on model calls per run. A full investigation in testing took
# 7 to 14 turns; 25 leaves room for retries without letting a stuck agent loop.
MAX_TURNS = 25

# OpenRouter prices in $ per million tokens (input, cached input, output),
# checked 2026-11-26. Used only for the cost estimate at the end of a run.
PRICES = {
    "deepseek/deepseek-v4.1-flash-1017": (0.15, 0.003, 0.60),
    "qwen/qwen3.6-35b-a3b": (0.10, 0.035, 0.89),
    "minimax/minimax-m3.1-flash": (0.075, 0.0075, 0.30),
}

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SYSTEM_PROMPT_PATH = os.path.join(SCRIPT_DIR, "SYSTEM_PROMPT.md")
TRACES_DIR = os.path.join(SCRIPT_DIR, "traces")

CONSOLE_PREVIEW = 160

# Parentheses are allowed inside a URL (Wikipedia uses them); curly quotes,
# dashes and ellipses are not, so prose right after a URL is not glued to it.
URL_PATTERN = re.compile(r"https?://[^\s<>\[\]\"'`|“”‘’—…]+")
TRACKING_PARAM = re.compile(r"^(utm_[a-z]+|lang|hl|ref|fbclid|gclid)=", re.IGNORECASE)


def urls_in(text):
    urls = set()
    for url in URL_PATTERN.findall(text):
        url = url.rstrip(".,;:*_")
        # A closing parenthesis belongs to the URL only if it opened one,
        # otherwise it ends a Markdown link or a sentence.
        while url.endswith(")") and url.count(")") > url.count("("):
            url = url[:-1].rstrip(".,;:*_")
        urls.add(url)
    return urls


def url_key(url):
    """Compare URLs ignoring a fragment, a trailing slash and tracking parameters
    such as ?lang=en, but not parameters that pick a different page (?v=...)."""
    url = url.split("#")[0]
    base, _, query = url.partition("?")
    kept = "&".join(p for p in query.split("&") if p and not TRACKING_PARAM.match(p))
    return base.rstrip("/") + ("?" + kept if kept else "")


def fence(text):
    # Pages often contain ``` themselves; the outer fence must be longer than
    # any backtick run inside or the code block ends early.
    longest = max((len(run) for run in re.findall(r"`+", text)), default=0)
    return "`" * max(3, longest + 1)


def one_line(text, limit=CONSOLE_PREVIEW):
    text = " ".join(str(text).split())
    return text if len(text) <= limit else text[: limit - 3] + "..."


class TraceLogger(RunHooks):
    """Write every model message, tool call and tool result to a Markdown trace file,
    and a one-line version of each to the terminal."""

    def __init__(self, path, header):
        self.path = path
        self.turn = 0
        self.tool_calls = Counter()
        self.input_tokens = 0
        self.cached_tokens = 0
        self.output_tokens = 0
        # Every URL the agent was shown or asked for, to check the report against.
        self.seen_urls = set()
        os.makedirs(os.path.dirname(path), exist_ok=True)
        self.file = open(path, "w", encoding="utf-8")
        self.write(header)

    def write(self, text):
        self.file.write(text + "\n")
        self.file.flush()

    def block(self, text, lang=""):
        f = fence(text)
        self.write(f"{f}{lang}\n{text}\n{f}")

    async def on_llm_start(self, context, agent, system_prompt, input_items):
        self.turn += 1
        self.write(f"\n## Turn {self.turn}\n")
        print(f"\n▶ Turn {self.turn}", file=sys.stderr)

    async def on_llm_end(self, context, agent, response):
        usage = response.usage
        self.input_tokens += usage.input_tokens
        self.cached_tokens += usage.input_tokens_details.cached_tokens or 0
        self.output_tokens += usage.output_tokens
        self.write(f"_Model call: {usage.input_tokens:,} input tokens, {usage.output_tokens:,} output tokens_\n")

        for item in response.output:
            kind = getattr(item, "type", "")
            if kind == "reasoning":
                # OpenRouter's reasoning text arrives in content, not summary.
                parts = list(item.summary or []) + list(getattr(item, "content", None) or [])
                summary = " ".join(getattr(p, "text", "") for p in parts)
                if summary.strip():
                    self.write("**Reasoning summary:**\n")
                    self.block(summary.strip())
            elif kind == "message":
                text = "".join(getattr(part, "text", "") for part in item.content)
                if text.strip():
                    self.write("**Assistant:**\n")
                    self.write(text.strip() + "\n")
                    print(f"  💬 {one_line(text)}", file=sys.stderr)
            elif kind == "function_call":
                self.tool_calls[item.name] += 1
                try:
                    args = json.loads(item.arguments or "{}")
                    pretty = json.dumps(args, indent=2, ensure_ascii=False)
                except json.JSONDecodeError:
                    args, pretty = {}, item.arguments
                self.write(f"**Tool call** `{item.name}` (id `{item.call_id}`):\n")
                self.block(pretty, "json")
                print(f"  🔧 {item.name}({one_line(self.call_summary(item.name, args), 120)})", file=sys.stderr)

    @staticmethod
    def call_summary(name, args):
        if name == "read_url":
            return f"{args.get('url')}" + (f", start={args['start']}" if args.get("start") else "")
        if name == "web_search":
            return repr(args.get("query"))
        if name == "save_report":
            return f"{args.get('filename')}, {len(args.get('markdown', '')):,} chars"
        if name == "assess_credibility":
            evaluation = args.get("evaluation", {})
            return f"overall_credibility={evaluation.get('overall_credibility')}"
        return json.dumps(args)

    async def on_tool_end(self, context, agent, tool, result):
        call_id = getattr(context, "tool_call_id", "?")
        text = result if isinstance(result, str) else json.dumps(result, indent=2, ensure_ascii=False)
        # Only successful results count. The agent's own arguments and error
        # messages echo the URL it asked for, which would let an invented URL
        # that 404s pass the check.
        if tool.name in ("read_url", "web_search") and not text.startswith("Error:"):
            self.seen_urls |= urls_in(text)
        self.write(f"**Tool result** `{tool.name}` (id `{call_id}`, {len(text):,} characters):\n")
        self.block(text)
        print(f"     ↳ {one_line(text, 110)}", file=sys.stderr)

    def close(self):
        self.file.close()


def load_system_prompt(with_assessment):
    with open(SYSTEM_PROMPT_PATH, "r", encoding="utf-8") as f:
        prompt = f.read().replace("{{TODAY}}", date.today().isoformat())
    if with_assessment:
        return re.sub(r"<!-- assess:(start|end) -->\n", "", prompt)
    # Ablation for reflection question 2: drop the tool and every mention of it.
    prompt = re.sub(r"<!-- assess:start -->.*?<!-- assess:end -->\n", "", prompt, flags=re.DOTALL)
    prompt = prompt.replace("## Structured Assessment\n<every field of the assessment as a table or list>\n", "")
    prompt = prompt.replace("record a structured assessment, and save", "and save")
    return prompt.replace("## 7. Report", "## 6. Report")


def trace_path(url, suffix):
    parsed = urlparse(url)
    slug = re.sub(r"[^a-z0-9]+", "-", (parsed.netloc + parsed.path).lower()).strip("-")[:60]
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    return os.path.join(TRACES_DIR, f"{stamp}-{slug}{suffix}.md")


def unverified_urls(report_path, seen_urls):
    """URLs in the saved report that never appeared in a tool call or tool result."""
    with open(report_path, encoding="utf-8") as f:
        cited = urls_in(f.read())
    seen = {url_key(u) for u in seen_urls}
    return sorted(u for u in cited if url_key(u) not in seen)


def estimate_cost(model, logger):
    if model not in PRICES:
        return None
    price_in, price_cached, price_out = PRICES[model]
    uncached = logger.input_tokens - logger.cached_tokens
    return (uncached * price_in + logger.cached_tokens * price_cached + logger.output_tokens * price_out) / 1e6


def parse_args():
    parser = argparse.ArgumentParser(
        prog="credibility-agent",
        description="Investigate a web source and write a Markdown credibility report.",
    )
    parser.add_argument("url", help="The URL of the source to evaluate")
    parser.add_argument("--max-turns", type=int, default=MAX_TURNS, help=f"Maximum model calls (default {MAX_TURNS})")
    parser.add_argument("--model", default=MODEL, help=f"OpenRouter model ID (default {MODEL})")
    parser.add_argument(
        "--no-assess",
        action="store_true",
        help="Run without the assess_credibility tool, to compare reports with and without it",
    )
    args = parser.parse_args()
    if args.max_turns < 3:
        parser.error("--max-turns must be at least 3 (read, assess, save)")
    if not args.url.startswith(("http://", "https://")):
        parser.error("the URL must start with http:// or https://")
    return args


async def main():
    args = parse_args()

    load_dotenv(find_dotenv(usecwd=True))
    missing = [key for key in ("OPENROUTER_API_KEY", "TAVILY_API_KEY") if not os.getenv(key)]
    if missing:
        print(f"❌ Missing {', '.join(missing)}. Add it to the .env file (see README.md).", file=sys.stderr)
        sys.exit(1)

    # The Agents SDK talks to OpenAI by default. Point it at OpenRouter, use Chat
    # Completions (OpenRouter has no Responses API for these models), and turn
    # off OpenAI's hosted tracing, which an OpenRouter key cannot log in to.
    client = AsyncOpenAI(base_url="https://openrouter.ai/api/v1", api_key=os.environ["OPENROUTER_API_KEY"])
    set_default_openai_client(client, use_for_tracing=False)
    set_default_openai_api("chat_completions")
    set_tracing_disabled(True)

    with_assessment = not args.no_assess
    tools = [read_url, web_search] + ([assess_credibility] if with_assessment else []) + [save_report]
    agent = Agent(
        name="Source Credibility Analyst",
        instructions=load_system_prompt(with_assessment),
        tools=tools,
        # A bare "deepseek/..." string makes the SDK look for a provider called
        # "deepseek", so the OpenRouter model ID is wrapped in a model object.
        model=OpenAIChatCompletionsModel(model=args.model, openai_client=client),
    )
    info = RunInfo(require_assessment=with_assessment)

    path = trace_path(args.url, "" if with_assessment else "-no-assess")
    header = (
        f"# Agent trace: {args.url}\n\n"
        f"- Model: `{args.model}`\n"
        f"- Started: {datetime.now().isoformat(timespec='seconds')}\n"
        f"- Max turns: {args.max_turns}\n"
        f"- Tools: {', '.join(t.name for t in tools)}\n"
    )
    logger = TraceLogger(path, header)
    logger.seen_urls.add(args.url)
    prompt = f"Evaluate the credibility of this source: {args.url}"
    logger.write(f"\n**User:** {prompt}")
    print(f"🔎 {prompt}\n   model {args.model}, max {args.max_turns} turns", file=sys.stderr)

    final_output = None
    exit_code = 0
    try:
        result = await Runner.run(agent, prompt, context=info, max_turns=args.max_turns, hooks=logger)
        final_output = result.final_output
    except MaxTurnsExceeded:
        logger.write(f"\n## Stopped\n\nThe run hit the limit of {args.max_turns} turns before the agent finished.")
        print(f"\n⚠️  Stopped after {args.max_turns} turns without finishing.", file=sys.stderr)
        exit_code = 1
    except APIError as err:
        logger.write(f"\n## Stopped\n\nOpenRouter error: {err}")
        print(f"\n❌ OpenRouter error: {err}", file=sys.stderr)
        exit_code = 1
    except AgentsException as err:
        # For example ModelBehaviorError when the model calls a tool that does
        # not exist or OpenRouter answers with an error body. The summary below
        # still gets written, so the trace shows how far the run got.
        logger.write(f"\n## Stopped\n\n{type(err).__name__}: {err}")
        print(f"\n❌ {type(err).__name__}: {err}", file=sys.stderr)
        exit_code = 1
    except (asyncio.CancelledError, KeyboardInterrupt):
        logger.write("\n## Stopped\n\nInterrupted (Ctrl+C).")
        print("\n⚠️  Interrupted.", file=sys.stderr)
        exit_code = 130

    cost = estimate_cost(args.model, logger)
    calls = ", ".join(f"{name} x{count}" for name, count in logger.tool_calls.most_common()) or "none"
    summary = [
        f"Turns (model calls): {logger.turn}",
        f"Tool calls: {calls}",
        f"Tokens: {logger.input_tokens:,} input ({logger.cached_tokens:,} cached), {logger.output_tokens:,} output",
        f"Estimated cost: ${cost:.4f}" if cost is not None else "Estimated cost: unknown for this model",
        "Report: " + (", ".join(os.path.relpath(p, SCRIPT_DIR) for p in info.reports) or "not saved"),
    ]
    for report in info.reports:
        unverified = unverified_urls(report, logger.seen_urls)
        line = f"URLs in {os.path.basename(report)} not seen in any tool result: "
        summary.append(line + (", ".join(unverified) if unverified else "none"))
    if final_output:
        logger.write(f"\n## Final output\n\n{final_output}")
    logger.write("\n## Summary\n\n" + "\n".join(f"- {line}" for line in summary))
    logger.close()

    print("\n" + "-" * 60, file=sys.stderr)
    for line in summary + [f"Trace: {os.path.relpath(path, SCRIPT_DIR)}"]:
        print(line, file=sys.stderr)
    if final_output:
        print("-" * 60, file=sys.stderr)
        print(final_output)
    if not info.reports:
        print("⚠️  The agent did not save a report.", file=sys.stderr)
        exit_code = exit_code or 1
    sys.exit(exit_code)


if __name__ == "__main__":
    asyncio.run(main())
