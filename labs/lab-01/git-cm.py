#!/usr/bin/env python3
import os
import sys
import subprocess
from datetime import datetime

from dotenv import load_dotenv, find_dotenv
from openai import OpenAI

STUDENT_NAME = "Nattharut Natvongsakul"
STUDENT_ID = "184108231"

# Two free models from two different providers on OpenRouter.
MODEL_A = "google/gemma-3-27b-it:free"
MODEL_B = "meta-llama/llama-3.3-70b-instruct:free"
DEFAULT_MODEL = MODEL_A

DEFAULT_TEMPERATURE = 0.1
CREATIVE_TEMPERATURE = 1.3

DEFAULT_SYSTEM_PROMPT = (
    "You are an LLM running in a CLI tool, which writes semantic commit messages "
    "for the user. You will be given a git diff. You must output ONLY the commit "
    "message using the Conventional Commits standard format "
    "(e.g., 'feat: add logging').\n\n"
    "Respond in plain text suitable for pasting into git commit -m "
    "'...your commit message...'; just the plain text commit message with no "
    "Markdown, no rationale about why you chose it, etc."
)

CREATIVE_SYSTEM_PROMPT = (
    "You are an LLM running in a CLI tool, which writes semantic commit messages "
    "for the user. You will be given a git diff. Write the commit message using "
    "Gitmoji and 17th century pirate slang, keeping it as fun and flavorful as "
    "possible while still starting with a Conventional Commits type "
    "(e.g., 'feat', 'fix').\n\n"
    "Respond in plain text suitable for pasting into git commit -m "
    "'...your commit message...'; just the plain text commit message with no "
    "Markdown, no rationale about why you chose it, etc."
)


def print_header():
    run_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("AIP444 Fall 2026 - Lab 01")
    print(f"git-cm: Developed by {STUDENT_NAME} - {STUDENT_ID}")
    print(f"Run Date: {run_date}")
    print("-" * 60)


def load_api_key():
    load_dotenv(find_dotenv())
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        print("❌ Error: OPENROUTER_API_KEY not found")
        sys.exit(1)
    return api_key


def get_staged_diff():
    try:
        result = subprocess.run(
            ["git", "diff", "--staged"], capture_output=True, text=True, check=True
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Not a git repo.")
        sys.exit(1)

    diff = result.stdout.strip()
    if not diff:
        print("❌ No staged changes found")
        sys.exit(1)

    print(f"✅ Diff found: {len(diff)} characters")
    return diff


def generate_commit_message(client, model, system_prompt, temperature, diff):
    response = client.chat.completions.create(
        model=model,
        temperature=temperature,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": diff},
        ],
    )
    return response.choices[0].message.content.strip()


def main():
    print_header()
    api_key = load_api_key()
    diff = get_staged_diff()

    is_creative = "--creative" in sys.argv

    client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)

    if is_creative:
        print(f"\nCreative mode enabled (temperature={CREATIVE_TEMPERATURE})\n")

        message_a = generate_commit_message(
            client, MODEL_A, CREATIVE_SYSTEM_PROMPT, CREATIVE_TEMPERATURE, diff
        )
        message_b = generate_commit_message(
            client, MODEL_B, CREATIVE_SYSTEM_PROMPT, CREATIVE_TEMPERATURE, diff
        )

        print(f"Option 1 ({MODEL_A}):\n{message_a}\n")
        print(f"Option 2 ({MODEL_B}):\n{message_b}")
    else:
        message = generate_commit_message(
            client, DEFAULT_MODEL, DEFAULT_SYSTEM_PROMPT, DEFAULT_TEMPERATURE, diff
        )
        print(f"\nGenerated commit message:\n\n{message}")


if __name__ == "__main__":
    main()
