def ask_drug(collection, model, drug, question, k=5):
    embedding = model.encode(question).tolist()

    results = collection.query(
        query_embeddings=[embedding],
        n_results=k,
        where={"drug": drug.lower()}
    )

    return "\n".join(results["documents"][0])