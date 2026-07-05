import chromadb
from backend.knowledge_base import SKILL_BENCHMARKS

# Persistent client = stores data on disk, not just in memory
chroma_client = chromadb.PersistentClient(path="./chroma_data")

collection = chroma_client.get_or_create_collection(name="skill_benchmarks")


def load_knowledge_base():
    """Loads all skill benchmark docs into ChromaDB. Safe to call multiple times."""
    existing_ids = set(collection.get()["ids"])

    documents = []
    ids = []

    for doc in SKILL_BENCHMARKS:
        if doc["id"] not in existing_ids:
            documents.append(doc["text"])
            ids.append(doc["id"])

    if documents:
        collection.add(documents=documents, ids=ids)
        print(f"Added {len(documents)} new documents to ChromaDB.")
    else:
        print("Knowledge base already loaded, nothing new to add.")


def search_benchmarks(query_text: str, top_k: int = 3):
    """Given a query (e.g. user's profile summary), return the most relevant benchmark docs."""
    results = collection.query(query_texts=[query_text], n_results=top_k)
    return results["documents"][0]  # list of matched document texts