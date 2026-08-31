import re

def split_text(text, max_length=500, min_length=20):
    if not text:
        return []
    
    raw_paragraphs = text.split("\n\n")

    if len(raw_paragraphs) <= 1:
        raw_paragraphs = text.split("\n")

    chunks = []
    chunk_id = 1
    for p in raw_paragraphs:
        p = p.strip()

        if len(p) < min_length:
            continue

        if len(p) > max_length:
            for i in range(0, len(p), max_length):
                sub_p = p[i:i + max_length]
                chunks.append({
                    "id": chunk_id,
                    "text": sub_p
                })
                chunk_id += 1
        else:
            chunks.append({
                "id": chunk_id,
                "text": p
            })
            chunk_id += 1

    return chunks


def split_text_by_article(text, source="Unknown"):
    articles = re.split(r'(?=\n第\s*[0-9一二三四五六七八九十]+\s*條)', text)
    
    chunks = []
    for idx, article in enumerate(articles, start=1):
        content = article.strip()
        
        if len(content) <= 30:
            continue

        match = re.search(
            r'第\s*[0-9一二三四五六七八九十]+\s*條',
            content
        )
        if match:
            article_number = match.group()
        else:
            article_number = f"Chunk {idx}"

        chunks.append({
            "id": idx,
            "article": article_number,
            "source": source,
            "text": content
        })
    return chunks

def split_documents(documents):
    all_chunks = []

    chunk_id = 1

    for document in documents:

        source = document["source"]
        text = document["text"]

        chunks = split_text_by_article(
            text,
            source=source
        )

        for chunk in chunks:

            chunk["id"] = chunk_id

            all_chunks.append(chunk)

            chunk_id += 1

    return all_chunks