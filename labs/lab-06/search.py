from utils import load_database, search_products


def main():
    products = load_database()
    print(f"Loaded {len(products)} products. Press Enter on an empty line to quit.")

    while True:
        try:
            query = input("\nWhat are you looking for? ").strip()
        except EOFError:
            break
        if not query or query.lower() == "quit":
            break

        results = search_products(query, products)
        if not results:
            print("I'm sorry, we don't have anything like that in stock.")
            continue

        print(f"Found {len(results)} matches:")
        for i, p in enumerate(results, 1):
            print(
                f"{i}. [Rerank: {p['rerank_score']:.2f} | Vector: {p['vector_score']:.2f}] "
                f"{p['title']} - ${p['price']:.2f}"
            )


if __name__ == "__main__":
    main()
