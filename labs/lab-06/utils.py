import json
import os

import requests
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI

EMBEDDING_MODEL = "openai/text-embedding-3-small"
RERANK_MODEL = "cohere/rerank-v3.5"

# threshold.py: "Nice smelling scent" tops out at 0.41, "A textbook on quantum
# physics" at 0.149. Long conversational queries score much lower than short
# ones (the back-pain query's best product is 0.206), so this gate only throws
# out queries that match nothing at all.
MIN_SIMILARITY_SCORE = 0.15

# Vector scores can't separate the README test queries ("luxury boat" scores
# 0.298, above two real matches), so relevance is decided on the cross-encoder
# score instead. Happy-path queries topped out at 0.094-0.473, out-of-domain
# ones at 0.025-0.064 (plus 0.160 for "vegan cat food", which matches Cat Food).
MIN_RERANK_SCORE = 0.08

# The reranker can only promote what vector search retrieved, so retrieve more
# than we show.
CANDIDATES = 20
TOP_N = 5

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PRODUCTS_PATH = os.path.join(SCRIPT_DIR, "products.json")
VECTORS_PATH = os.path.join(SCRIPT_DIR, "vectors.tsv")
METADATA_PATH = os.path.join(SCRIPT_DIR, "metadata.tsv")

load_dotenv(find_dotenv())


def get_client():
    return OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.environ["OPENROUTER_API_KEY"],
    )


def serialize_product(product: dict) -> str:
    parts = [
        f"Title: {product['title']}",
        f"Category: {product['category']}",
        f"Description: {product['description']}",
        f"Tags: {', '.join(product.get('tags', []))}",
    ]
    # Some products (groceries, for example) have no brand.
    if product.get("brand"):
        parts.append(f"Brand: {product['brand']}")
    return " | ".join(parts)


def embed(texts: list[str]) -> list[list[float]]:
    response = get_client().embeddings.create(
        model=EMBEDDING_MODEL,
        input=texts,
        encoding_format="float",
    )
    return [item.embedding for item in response.data]


def dot_product(vec_a: list[float], vec_b: list[float]) -> float:
    return sum(a * b for a, b in zip(vec_a, vec_b))


def load_database():
    with open(PRODUCTS_PATH, "r", encoding="utf-8") as f:
        products = json.load(f)

    with open(VECTORS_PATH, "r", encoding="utf-8") as f:
        lines = f.read().strip().split("\n")

    products_with_embeddings = []
    for product, line in zip(products, lines):
        product["embedding"] = [float(x) for x in line.split("\t")]
        products_with_embeddings.append(product)

    return products_with_embeddings


def rank_by_similarity(query: str, products: list[dict]) -> list[tuple[float, dict]]:
    query_vector = embed([query])[0]
    scored = [(dot_product(query_vector, p["embedding"]), p) for p in products]
    scored.sort(key=lambda pair: pair[0], reverse=True)
    return scored


def rerank_results(query: str, candidates: list[dict], top_n: int = TOP_N) -> list[dict]:
    documents = [serialize_product(p) for p in candidates]

    response = requests.post(
        "https://openrouter.ai/api/v1/rerank",
        headers={
            "Authorization": f"Bearer {os.environ['OPENROUTER_API_KEY']}",
            "Content-Type": "application/json",
        },
        json={
            "model": RERANK_MODEL,
            "query": query,
            "documents": documents,
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


def search_products(
    query: str,
    products: list[dict],
    min_score: float = MIN_SIMILARITY_SCORE,
) -> list[dict]:
    candidates = [
        {**p, "vector_score": score}
        for score, p in rank_by_similarity(query, products)
        if score >= min_score
    ][:CANDIDATES]

    if not candidates:
        return []

    return [p for p in rerank_results(query, candidates) if p["rerank_score"] >= MIN_RERANK_SCORE]
