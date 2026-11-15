from utils import load_database, rank_by_similarity

QUERIES = [
    "Nice smelling scent",            # should exist (fragrances)
    "A textbook on quantum physics",  # should not exist
]


def main():
    products = load_database()
    for query in QUERIES:
        print(f'\nTop 3 for "{query}":')
        for score, product in rank_by_similarity(query, products)[:3]:
            print(f"  {score:.4f}  {product['title']} ({product['category']})")


if __name__ == "__main__":
    main()
