import json

import requests

from utils import embed, serialize_product

PRODUCTS_URL = "https://dummyjson.com/products?limit=200"


def clean(text: str) -> str:
    # A stray tab or newline would shift every column after it in the TSV.
    return text.replace("\t", " ").replace("\n", " ").replace("\r", " ")


def main():
    response = requests.get(PRODUCTS_URL, timeout=30)
    response.raise_for_status()
    products = response.json()["products"]
    print(f"Fetched {len(products)} products")

    with open("products.json", "w", encoding="utf-8") as f:
        json.dump(products, f, indent=2, ensure_ascii=False)

    texts = [serialize_product(p) for p in products]
    vectors = embed(texts)
    # load_database pairs line N with product N, so a short response would
    # silently attach the wrong vectors to every product after the gap.
    assert len(vectors) == len(products), f"{len(vectors)} vectors for {len(products)} products"
    print(f"Embedded {len(vectors)} products ({len(vectors[0])} dimensions)")

    with open("vectors.tsv", "w", encoding="utf-8") as f:
        f.write("\n".join("\t".join(str(x) for x in v) for v in vectors))

    with open("metadata.tsv", "w", encoding="utf-8") as f:
        f.write("Title\tCategory\n")
        f.write("\n".join(f"{clean(p['title'])}\t{clean(p['category'])}" for p in products))

    print("Wrote products.json, vectors.tsv, metadata.tsv")


if __name__ == "__main__":
    main()
