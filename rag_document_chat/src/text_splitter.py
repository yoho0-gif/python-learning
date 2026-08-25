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


def split_text_by_article(text):
    articles = re.split(r'(?=\n第\s*[0-9一二三四五六七八九十]+\s*條)', text)
    
    chunks = []
    for idx, article in enumerate(articles, start=1):
        content = article.strip()
        
        if content:
            chunks.append({
                "id": idx,
                "text": content
            })
            
    return chunks