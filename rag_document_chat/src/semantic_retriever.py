from embedding import create_embedding, cosine_similarity


def retrieve_similar_chunks(chunks, query, top_k=3):
    if not chunks or not query.strip():
        return []

    query_vector = create_embedding(query)

    scored_chunks = []

    for chunk in chunks:        
        score = cosine_similarity(
            query_vector,
            chunk["embedding"]
        )

        scored_chunks.append({
            "chunk": chunk,
            "score": score
        })

    scored_chunks.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return scored_chunks[:top_k]