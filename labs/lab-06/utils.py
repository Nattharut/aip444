import json
import os

import requests
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI

# From threshold.py: "Nice smelling scent" scored 0.41 against its best match,
# "A textbook on quantum physics" only 0.15.
MIN_SIMILARITY_SCORE = 0.30

load_dotenv(find_dotenv())

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"],
)


def serialize_product(product: dict) -> str:
    parts = [
        f"Title: {product['title']}",
        f"Category: {product['category']}",
        f"Description: {product['description']}",
        f"Tags: {', '.join(product['tags'])}",
    ]
    # Some products (groceries, for example) have no brand.
    if product.get("brand"):
        parts.append(f"Brand: {product['brand']}")
    return " | ".join(parts)


def embed(texts: list[str]) -> list[list[float]]:
    response = client.embeddings.create(
        model="openai/text-embedding-3-small",
        input=texts,
        encoding_format="float",
    )
    return [item.embedding for item in response.data]


def dot_product(vec_a: list[float], vec_b: list[float]) -> float:
    return sum(a * b for a, b in zip(vec_a, vec_b))


def load_database():
    # 1. Read the JSON file
    with open('products.json', 'r', encoding='utf-8') as f:
        products = json.load(f)

    # 2. Read the TSV file
    with open('vectors.tsv', 'r', encoding='utf-8') as f:
        vectors_data = f.read()
        lines = vectors_data.strip().split('\n')

    # 3. Attach vectors to products
    # Python's zip() function pairs the two lists automatically
    products_with_embeddings = []

    for product, line in zip(products, lines):
        # Convert tab-separated values to a list of floats
        vector = [float(x) for x in line.split('\t')]

        # Add the embedding to the product dictionary
        product['embedding'] = vector
        products_with_embeddings.append(product)

    return products_with_embeddings


def rerank_results(
    query: str,
    candidates: list[dict],
    top_n: int = 5
) -> list[dict]:
    documents = [
        serialize_product(p) for p in candidates
    ]

    response = requests.post(
        'https://openrouter.ai/api/v1/rerank',
        headers={
            'Authorization': f'Bearer {os.environ["OPENROUTER_API_KEY"]}',
            'Content-Type': 'application/json',
        },
        json={
            'model': 'cohere/rerank-v3.5',
            'query': query,
            'documents': documents,
            'top_n': top_n,
        },
    )

    data = response.json()

    return [
        {**candidates[r['index']],
         'rerank_score': r['relevance_score']}
        for r in data['results']
    ]


def search_products(
    query: str,
    products: list[dict],
    min_score: float = MIN_SIMILARITY_SCORE
) -> list[dict]:
    # 1. Embed the query
    query_embedding = embed([query])[0]

    # 2. Calculate dot product against all products
    scored = [(dot_product(query_embedding, p['embedding']), p) for p in products]

    # 3. Sort by score (descending)
    scored.sort(key=lambda pair: pair[0], reverse=True)

    # 4. Filter out anything below min_score
    scored = [(score, p) for score, p in scored if score >= min_score]

    # 5. Attach the vector score to each candidate
    candidates = [{**p, 'vector_score': score} for score, p in scored]

    # 6. Take top 20 candidates (wider net)
    candidates = candidates[:20]

    # 7. If no candidates, return []
    if not candidates:
        return []

    # 8. Rerank the candidates and return top 5
    return rerank_results(query, candidates, top_n=5)
