import os
import sys

import chromadb
import requests
from chromadb.errors import NotFoundError
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
from dotenv import load_dotenv

load_dotenv()

CHROMA_RESULTS = 25
RERANK_TOP_N = 5

# Same embedding model as indexer.py, so queries and chunks share one vector space
openai_ef = OpenAIEmbeddingFunction(
    api_key=os.environ["OPENROUTER_API_KEY"],
    model_name="openai/text-embedding-3-small",
    api_base="https://openrouter.ai/api/v1",
)

client = chromadb.PersistentClient(
    path=os.path.join(os.path.dirname(__file__), "chroma_db")
)


def retrieve(query: str, n_results: int = CHROMA_RESULTS) -> list[dict]:
    try:
        collection = client.get_collection(name="node-docs", embedding_function=openai_ef)
    except NotFoundError:
        sys.exit("The node-docs collection doesn't exist yet. Run: python indexer.py")

    # query_texts is embedded with openai_ef before the nearest-neighbour search
    results = collection.query(
        query_texts=[query],
        n_results=n_results,
        include=["documents", "metadatas", "distances"],
    )

    # Chroma returns one list per query text; we only sent one
    return [
        {
            "id": chunk_id,
            "content": document,
            "metadata": metadata,
            "distance": distance,
            "chroma_rank": rank,
        }
        for rank, (chunk_id, document, metadata, distance) in enumerate(
            zip(
                results["ids"][0],
                results["documents"][0],
                results["metadatas"][0],
                results["distances"][0],
            ),
            start=1,
        )
    ]


def rerank_results(query: str, candidates: list[dict], top_n: int = RERANK_TOP_N) -> list[dict]:
    if not candidates:
        return []

    response = requests.post(
        "https://openrouter.ai/api/v1/rerank",
        headers={
            "Authorization": f"Bearer {os.environ['OPENROUTER_API_KEY']}",
            "Content-Type": "application/json",
        },
        json={
            "model": "cohere/rerank-v3.5",
            "query": query,
            "documents": [c["content"] for c in candidates],
            "top_n": top_n,
        },
        timeout=60,
    )
    response.raise_for_status()
    data = response.json()

    return [
        {**candidates[r["index"]], "rerank_score": r["relevance_score"]}
        for r in data["results"]
    ]


def search(query: str, top_n: int = RERANK_TOP_N) -> list[dict]:
    return rerank_results(query, retrieve(query), top_n=top_n)


def main():
    query = " ".join(sys.argv[1:]).strip()
    if not query:
        print('Usage: python query.py "How do I read a file?"', file=sys.stderr)
        sys.exit(1)

    candidates = retrieve(query)
    results = rerank_results(query, candidates)

    print(f'Query: "{query}"')
    print(f"\nChroma top {len(candidates)} (before rerank):")
    for c in candidates:
        print(f"  #{c['chroma_rank']:<2} distance {c['distance']:.4f}  "
              f"{c['metadata']['source']}: {c['metadata']['breadcrumb']}")

    print(f"\nTop {len(results)} after rerank:")
    for i, r in enumerate(results, 1):
        # Cosine distance is 1 - cosine similarity
        similarity = 1 - r["distance"]
        print(f"\n{i}. {r['metadata']['breadcrumb']}")
        print(f"   source: {r['metadata']['source']}  |  chroma rank: #{r['chroma_rank']}  |  "
              f"distance: {r['distance']:.4f} (similarity {similarity:.4f})  |  "
              f"rerank: {r['rerank_score']:.4f}")
        body = r["content"].split("\n\n", 1)[-1]
        preview = " ".join(body.split())[:160]
        print(f"   {preview}...")


if __name__ == "__main__":
    main()
