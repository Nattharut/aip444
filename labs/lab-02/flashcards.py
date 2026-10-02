#!/usr/bin/env python3
import argparse
import os
import re
import sys
from datetime import datetime

from dotenv import load_dotenv, find_dotenv
from openai import OpenAI, APIStatusError

STUDENT_NAME = "Nattharut Natvongsakul"
STUDENT_ID = "184108231"

# Free instruction-following model first; cheap paid version if rate-limited (429)
# or otherwise unavailable.
DEFAULT_MODEL = "meta-llama/llama-3.3-70b-instruct:free"
FALLBACK_MODEL = "meta-llama/llama-3.3-70b-instruct"

TEMPERATURE = 0.2

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SYSTEM_PROMPT_PATH = os.path.join(SCRIPT_DIR, "SYSTEM_PROMPT.md")


def print_header():
    run_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("AIP444 Fall 2026 - Lab 02")
    print(f"flashcards: Developed by {STUDENT_NAME} - {STUDENT_ID}")
    print(f"Run Date: {run_date}")
    print("-" * 60)


def load_api_key():
    load_dotenv(find_dotenv())
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        print("❌ Error: OPENROUTER_API_KEY not found")
        sys.exit(1)
    return api_key


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Generate ACE flashcards from course notes"
    )
    parser.add_argument(
        "notes_path", help="Path to the notes file (Markdown, HTML, or text)"
    )
    parser.add_argument(
        "--cards",
        type=int,
        default=3,
        help="Number of flashcards to generate (1-5, default: 3)",
    )

    args = parser.parse_args()

    if args.cards < 1 or args.cards > 5:
        parser.error("--cards must be between 1 and 5")

    return args


def get_file_contents(path, description):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"❌ Error: {description} not found: {path}")
        sys.exit(1)
    except Exception as err:
        print(f"❌ Error reading {description}: {path}")
        print(f"   {err}")
        sys.exit(1)


def build_user_prompt(notes, num_cards):
    return (
        f"Generate {num_cards} ACE flashcard(s) from the course notes below.\n\n"
        f"<notes>\n{notes}\n</notes>"
    )


def generate(client, model, system_prompt, user_prompt):
    response = client.chat.completions.create(
        model=model,
        temperature=TEMPERATURE,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )
    return response


def generate_with_fallback(client, system_prompt, user_prompt):
    try:
        return generate(client, DEFAULT_MODEL, system_prompt, user_prompt)
    except APIStatusError as e:
        print(f"⚠️  {DEFAULT_MODEL} unavailable ({e.status_code}), retrying with fallback model {FALLBACK_MODEL}...")
        return generate(client, FALLBACK_MODEL, system_prompt, user_prompt)


CARD_PATTERN = re.compile(
    # A card runs from its header to a line containing only "===". If the model
    # forgets that closing line, stop at the next card header (or end of output)
    # instead of swallowing the next card's "===" as this card's terminator.
    r"^=== CARD \d+ ===\n.*?(?:^===[ \t]*$|(?=^=== CARD )|\Z)",
    re.DOTALL | re.MULTILINE,
)


def extract_cards(output):
    return [card.strip() for card in CARD_PATTERN.findall(output)]


def main():
    print_header()
    api_key = load_api_key()
    args = parse_arguments()

    system_prompt = get_file_contents(SYSTEM_PROMPT_PATH, "System prompt file")
    notes = get_file_contents(args.notes_path, "Notes file")
    print(f"✅ Notes loaded: {args.notes_path} ({len(notes)} characters)")
    print(f"Generating {args.cards} card(s)...")

    client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)
    response = generate_with_fallback(
        client, system_prompt, build_user_prompt(notes, args.cards)
    )
    output = response.choices[0].message.content or ""

    if response.usage:
        print(
            f"Model: {response.model} | Tokens: {response.usage.prompt_tokens} in, "
            f"{response.usage.completion_tokens} out"
        )

    cards = extract_cards(output)
    if not cards:
        # No cards usually means the model judged the notes insufficient;
        # show its explanation instead of failing silently.
        print("\n❌ No cards found in output. Model response:\n")
        print(output.strip())
        sys.exit(1)

    print(f"\n✅ Generated {len(cards)} flashcard(s):\n")
    for card in cards:
        print(card)
        print()


if __name__ == "__main__":
    main()
