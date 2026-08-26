def retrieve_chunks(chunks, query, top_k=3):
    if not chunks or not query.strip():
        return []

    keywords = query.strip().lower().split()
    scored_chunks = []

    for chunk in chunks:
        text = chunk["text"] if isinstance(chunk, dict) else chunk
        text_lower = text.lower()

        score = 0
        for kw in keywords:
            count = text_lower.count(kw)
            score += count

        if score > 0:
            scored_chunks.append({"chunk": chunk, "score": score})

    scored_chunks.sort(key=lambda x: x["score"], reverse=True)
    top_results = scored_chunks[:top_k]

    return top_results