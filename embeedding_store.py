import json
import chromadb
from sentence_transformers import SentenceTransformer

def build_vector_store():
    client = chromadb.Client()
    collection = client.create_collection("drug_labels")

    model = SentenceTransformer("all-MiniLM-L6-v2")

    with open("data/processed_labels.json", "r") as f:
        docs = json.load(f)

    batch_size = 128
    for i in range(0, len(docs), batch_size):
        batch = docs[i:i + batch_size]

        texts = [d["text"] for d in batch]
        embeddings = model.encode(texts).tolist()

        collection.add(
            documents=texts,
            metadatas=[{"drug": d["drug"], "section": d["section"]} for d in batch],
            embeddings=embeddings,
            ids=[str(i + j) for j in range(len(batch))]
        )

    return collection, model