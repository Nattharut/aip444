#!/usr/bin/env python3
import argparse
import base64
import io
import os
import re
import sys
from datetime import date

from dotenv import find_dotenv, load_dotenv
from openai import APIError, OpenAI, pydantic_function_tool
from PIL import Image, ImageOps, UnidentifiedImageError
from pydantic import BaseModel, Field, ValidationError
from tavily import TavilyClient
from tavily.errors import InvalidAPIKeyError, UsageLimitExceededError

MODEL = "anthropic/claude-haiku-5.5"

# Defaults from the handout. Both can be changed per run with --max-side and
# --quality to see how far the image can shrink before the model misreads it.
MAX_SIDE = 1024
JPEG_QUALITY = 85

# Model calls per screenshot. The last call is made with tool_choice="none",
# so at most MAX_ITERATIONS - 1 rounds of searching can happen.
MAX_ITERATIONS = 5
SEARCH_RESULTS = 5

DEFAULT_PROMPT = "What is the error in this screenshot, and how do I fix it?"

FINAL_ANSWER_NUDGE = {
    "role": "user",
    "content": (
        "You cannot search any more. Write your final answer now, in the output format, "
        "using only what you already have. If that is not enough, say so in Cause."
    ),
}

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SYSTEM_PROMPT_PATH = os.path.join(SCRIPT_DIR, "SYSTEM_PROMPT.md")

URL_PATTERN = re.compile(r"https?://[^\s<>()\[\]\"'`]+")
LOCAL_URL = re.compile(r"https?://(localhost|127\.0\.0\.1|0\.0\.0\.0)([:/]|$)")


class LookupErrorArgs(BaseModel):
    query: str = Field(description="The search query to use based on the screenshot")


LOOKUP_ERROR_TOOL = pydantic_function_tool(
    LookupErrorArgs,
    name="lookup_error",
    description=(
        "Searches the web for technical documentation, coding errors, and other "
        "details to help with debugging the error."
    ),
)


def log(message=""):
    # stdout is reserved for the final answer, so it can be piped or saved.
    print(message, file=sys.stderr)


def human_size(num_bytes):
    if num_bytes < 1024:
        return f"{num_bytes} B"
    if num_bytes < 1024 * 1024:
        return f"{num_bytes / 1024:.1f} KB"
    return f"{num_bytes / (1024 * 1024):.2f} MB"


def process_image(path, max_side=MAX_SIDE, quality=JPEG_QUALITY):
    """Shrink the screenshot to fit max_side, re-encode it as JPEG, and return it base64-encoded."""
    original_bytes = os.path.getsize(path)
    with Image.open(path) as img:
        original_format = img.format
        img = ImageOps.exif_transpose(img)  # Fix phone photo rotation
        original_dimensions = img.size
        if img.mode in ("RGBA", "LA", "P"):
            # JPEG has no alpha channel, so transparent areas go on white
            # instead of the black that a plain convert("RGB") gives them.
            img = img.convert("RGBA")
            bg = Image.new("RGB", img.size, (255, 255, 255))
            bg.paste(img, mask=img.getchannel("A"))
            img = bg
        else:
            img = img.convert("RGB")
        img.thumbnail((max_side, max_side))  # Proportional, shrink-only
        buffer = io.BytesIO()
        img.save(buffer, format="JPEG", quality=quality)

    jpeg_bytes = buffer.getvalue()
    encoded = base64.b64encode(jpeg_bytes).decode("utf-8")

    width, height = original_dimensions
    log(f"Original:  {width}x{height} {original_format}, {human_size(original_bytes)} ({original_bytes:,} bytes)")
    log(f"Processed: {img.width}x{img.height} JPEG q{quality}, {human_size(len(jpeg_bytes))} ({len(jpeg_bytes):,} bytes)")
    log(f"Base64:    {len(encoded):,} characters")
    log(f"Base64 is {100 * len(encoded) / original_bytes:.1f}% of the original file size")
    return encoded


def load_system_prompt():
    with open(SYSTEM_PROMPT_PATH, "r", encoding="utf-8") as f:
        return f.read().replace("{{TODAY}}", date.today().isoformat())


def format_results(query, response, first_number):
    """Turn a Tavily response into the numbered list the system prompt describes."""
    results = response.get("results", [])
    if not results:
        return f'No web results for "{query}". Try different words, or answer without a search.', []

    lines = [f'Web search results for "{query}" (searched {date.today().isoformat()}):']
    for i, result in enumerate(results, first_number):
        lines.append("")
        lines.append(f"[{i}] {result.get('title') or '(untitled)'}")
        lines.append(f"URL: {result['url']}")
        if result.get("published_date"):
            lines.append(f"Published: {result['published_date']}")
        lines.append(f"Excerpt: {(result.get('content') or '').strip()}")
    return "\n".join(lines), results


def lookup_error(tavily, query, first_number=1):
    """Search with Tavily and return (text_for_the_model, results).

    Results are numbered from first_number, so a second search in the same run
    continues the numbering and [n] in the answer points at exactly one page.
    """
    log(f'🔎 Searching Tavily for "{query}"...')
    try:
        response = tavily.search(query=query, search_depth="basic", max_results=SEARCH_RESULTS)
    except (InvalidAPIKeyError, UsageLimitExceededError) as err:
        # Retrying can't help with a bad key or an empty quota, so stop here
        # instead of spending more model calls.
        log(f"❌ Tavily refused the search: {err}")
        sys.exit(1)
    except Exception as err:
        log(f"⚠️  Search failed: {type(err).__name__}: {err}")
        return f"Error: the search failed ({type(err).__name__}). Answer with what you already know and say that the search failed.", []

    text, results = format_results(query, response, first_number)
    for i, result in enumerate(results, first_number):
        log(f"   [{i}] {result['url']}")
    return text, results


def run_tool_call(tool_call, tavily, first_number):
    """Return (tool_message_content, query, results) for one tool call. query is None if nothing was searched."""
    name = tool_call.function.name
    if name != "lookup_error":
        return f"Error: there is no tool named {name!r}. The only tool is lookup_error.", None, []
    try:
        args = LookupErrorArgs.model_validate_json(tool_call.function.arguments or "{}")
    except ValidationError as err:
        return f'Error: invalid arguments ({err.errors()[0]["msg"]}). Send {{"query": "..."}}.', None, []
    query = args.query.strip()
    if not query:
        return "Error: the query was empty. Send the error message you want to search for.", None, []
    content, results = lookup_error(tavily, query, first_number)
    return content, query, results


def debug_screenshot(client, tavily, image_b64, prompt):
    """Run the tool-calling loop. Return (answer, finish_reason, queries, urls_from_search)."""
    messages = [
        {"role": "system", "content": load_system_prompt()},
        {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_b64}"}},
            ],
        },
    ]
    queries = []
    urls = set()
    results_so_far = 0
    total_cost = 0.0

    for iteration in range(1, MAX_ITERATIONS + 1):
        # On the last call the model may not search any more, so it has to
        # answer with what it has instead of the loop ending without an answer.
        # tool_choice="none" alone is not enough: Haiku 5.5 then returned only
        # hidden reasoning and content=None, so it is also told in words.
        last = iteration == MAX_ITERATIONS
        try:
            response = client.chat.completions.create(
                model=MODEL,
                messages=messages + [FINAL_ANSWER_NUDGE] if last else messages,
                tools=[LOOKUP_ERROR_TOOL],
                tool_choice="none" if last else "auto",
            )
        except APIError as err:
            log(f"❌ OpenRouter error: {err}")
            sys.exit(1)
        # OpenRouter can answer HTTP 200 with an error object and no choices.
        if not response.choices:
            log(f"❌ No response from the model: {(response.model_extra or {}).get('error')}")
            sys.exit(1)

        usage = response.usage
        if usage:
            cost = (usage.model_extra or {}).get("cost") or 0
            total_cost += cost
            log(f"🤖 Call {iteration}: {usage.prompt_tokens:,} tokens in, {usage.completion_tokens:,} out, ${cost:.5f}")

        message = response.choices[0].message
        # A provider can ignore tool_choice="none". On the last call, take
        # whatever text came back rather than running searches nobody reads.
        if not message.tool_calls or last:
            log(f"💵 Total: ${total_cost:.5f} over {iteration} call(s)")
            return message.content or "", response.choices[0].finish_reason, queries, urls

        # The model often says what it saw before it searches; show it as progress.
        if message.content and message.content.strip():
            log(f"💬 {message.content.strip()}")

        # The assistant message with its tool_calls has to stay in the history,
        # or the tool results that follow have nothing to answer.
        messages.append(message)
        for tool_call in message.tool_calls:
            content, query, results = run_tool_call(tool_call, tavily, results_so_far + 1)
            if query:
                queries.append(query)
            results_so_far += len(results)
            urls.update(r["url"] for r in results)
            messages.append({"role": "tool", "tool_call_id": tool_call.id, "content": content})


def check_references(answer, urls_from_search):
    """Warn about URLs in the answer that no search returned, since the model may have made them up."""
    cited = {url.rstrip(".,;:") for url in URL_PATTERN.findall(answer)}
    # Local addresses copied from the screenshot (a dev server, an API on
    # localhost) are not references, so they are not worth a warning.
    cited = {url for url in cited if not LOCAL_URL.match(url)}
    unverified = sorted(cited - urls_from_search)
    if unverified:
        log("⚠️  These URLs in the answer did not come from a search in this run, so check them before trusting them:")
        for url in unverified:
            log(f"   {url}")


def parse_args():
    parser = argparse.ArgumentParser(
        prog="img-debug",
        description="Explain and fix the error in a screenshot, using a vision model and Tavily web search.",
    )
    parser.add_argument("image", help="Path to the screenshot (PNG, JPEG, WebP, ...)")
    parser.add_argument("prompt", nargs="*", help="Optional note for the model, e.g. what you were trying to do")
    parser.add_argument("--max-side", type=int, default=MAX_SIDE, help=f"Longest side after resizing, in pixels (default {MAX_SIDE})")
    parser.add_argument("--quality", type=int, default=JPEG_QUALITY, help=f"JPEG quality, 1-95 (default {JPEG_QUALITY})")
    args = parser.parse_args()
    if not 1 <= args.quality <= 95:
        parser.error("--quality must be between 1 and 95")
    if args.max_side < 64:
        parser.error("--max-side must be at least 64")
    return args


def main():
    args = parse_args()

    load_dotenv(find_dotenv(usecwd=True))
    missing = [key for key in ("OPENROUTER_API_KEY", "TAVILY_API_KEY") if not os.getenv(key)]
    if missing:
        log(f"❌ Missing {', '.join(missing)}. Add it to the .env file (see README.md).")
        sys.exit(1)

    try:
        image_b64 = process_image(args.image, args.max_side, args.quality)
    except FileNotFoundError:
        log(f"❌ File not found: {args.image}")
        sys.exit(1)
    except UnidentifiedImageError:
        log(f"❌ Not an image Pillow can read: {args.image}")
        sys.exit(1)
    except OSError as err:
        # A folder, a file without read permission, or a truncated image.
        log(f"❌ Could not read {args.image}: {err}")
        sys.exit(1)

    prompt = " ".join(args.prompt).strip() or DEFAULT_PROMPT
    client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=os.environ["OPENROUTER_API_KEY"])
    tavily = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])

    log(f"🖼️  Sending the screenshot to {MODEL}...")
    answer, finish_reason, queries, urls = debug_screenshot(client, tavily, image_b64, prompt)
    if not answer.strip():
        log(f"❌ The model returned an empty answer (finish reason: {finish_reason})")
        sys.exit(1)

    log(f"📚 Searches: {len(queries)}" + (f" ({'; '.join(queries)})" if queries else ""))
    check_references(answer, urls)
    log("-" * 60)
    print(answer)
    if finish_reason == "length":
        log("⚠️  The answer hit the token limit and is cut off.")


if __name__ == "__main__":
    main()
