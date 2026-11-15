from utils import dot_product, embed, load_database

QUERIES = [
    "Nice smelling scent",            # should exist (fragrances)
    "A textbook on quantum physics",  # should not exist
]


def main():
    products = load_database()
    for query in QUERIES:
        query_embedding = embed([query])[0]
        scored = [(dot_product(query_embedding, p['embedding']), p) for p in products]
        scored.sort(key=lambda pair: pair[0], reverse=True)

        print(f'\nTop 3 for "{query}":')
        for score, product in scored[:3]:
            print(f"  {score:.4f}  {product['title']} ({product['category']})")


if __name__ == "__main__":
    main()
