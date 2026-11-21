import os
import glob
import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
from chunker import chunk_markdown
from dotenv import load_dotenv

load_dotenv()

# Custom embedding function using OpenRouter
openai_ef = OpenAIEmbeddingFunction(
    api_key=os.environ["OPENROUTER_API_KEY"],
    model_name="openai/text-embedding-3-small",
    api_base="https://openrouter.ai/api/v1",
)

client = chromadb.PersistentClient(
    path=os.path.join(os.path.dirname(__file__), "chroma_db")
)

def main():
    # 1. Initialize Chroma Collection, using our custom embedding function
    collection = client.get_or_create_collection(
        name="node-docs",
        embedding_function=openai_ef,
        configuration={
            "hnsw": {
                "space": "cosine",
            }
        },
    )

    # 2. Read files
    docs_dir = os.path.join(os.path.dirname(__file__), "docs")
    files = sorted(glob.glob(os.path.join(docs_dir, "*.md")))

    total_chunks = 0
    for filepath in files:
        filename = os.path.basename(filepath)

        print(f"Processing {filename}...")
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()

        # 3. Chunk
        chunks = chunk_markdown(text, filename)

        if len(chunks) == 0:
            continue

        # 4. Embed & Store
        ids = [c["id"] for c in chunks]
        documents = [c["content"] for c in chunks]
        metadatas = [c["metadata"] for c in chunks]

        # Add to collection (embeds automatically via embedding_function).
        # upsert instead of add, so a rerun after a failed run doesn't
        # stop on IDs that are already stored.
        collection.upsert(
            ids=ids,
            documents=documents,
            metadatas=metadatas,
        )
        total_chunks += len(chunks)

    print(f"Indexing complete! {total_chunks} chunks from {len(files)} files, "
          f"{collection.count()} in the collection.")

if __name__ == "__main__":
    main()
