import os
import sys

from dotenv import load_dotenv
from openai import OpenAI

from query import search

load_dotenv()

MODEL = "google/gemini-3.1-flash-lite-preview"

# Chunks passed to the LLM after reranking the top 25 from Chroma.
CONTEXT_CHUNKS = 5

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"],
)


def attr(value: str) -> str:
    # A few breadcrumbs hold " or < (e.g. `--experimental-package-map=<path>`),
    # which would break the attribute. > is left alone: it is the breadcrumb
    # separator, and &gt; in every citation would only confuse the model.
    return value.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;")


def build_system_prompt(chunks: list[dict]) -> str:
    # The chunk content stays raw so code samples are readable. It comes from
    # the Node docs, and none of the chunks contains </doc> or </context>.
    docs = "\n".join(
        f'  <doc source="{attr(c["metadata"]["source"])}" '
        f'breadcrumb="{attr(c["metadata"]["breadcrumb"])}">\n'
        f"{c['content']}\n"
        f"  </doc>"
        for c in chunks
    )

    return f"""You are ask-node, an expert node.js assistant that answers questions about Node.js.

Here is some context from the official documentation:

<context>
{docs}
</context>

Instructions:
1. Answer the user's question based ONLY on the provided context. Do not add APIs, options, or behaviour that the context does not mention, even if you know them.
2. If the answer is not in the context, say "I don't have enough information to answer that." and nothing else.
3. Cite the source file(s) (e.g., fs.md) for your information.
4. Keep code examples short and use only APIs shown in the context."""


def main():
    question = " ".join(sys.argv[1:]).strip()
    if not question:
        print('Usage: python ask-node.py "How do I read a file?"', file=sys.stderr)
        sys.exit(1)

    # Retrieve (top 25 from Chroma) and rerank down to the best few
    chunks = search(question, top_n=CONTEXT_CHUNKS)

    # Sources go to stderr so stdout holds only the answer
    print("Sources:", file=sys.stderr)
    for c in chunks:
        print(f"  [{c['rerank_score']:.3f}] {c['metadata']['source']}: "
              f"{c['metadata']['breadcrumb']}", file=sys.stderr)
    print(file=sys.stderr)

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": build_system_prompt(chunks)},
            {"role": "user", "content": question},
        ],
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
