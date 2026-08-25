from embedding import create_embedding
from vector_store import save_vectors, load_vectors


def build_embeddings(chunks, path):
    stored_vectors = load_vectors(path)

    if stored_vectors:
        print("找到既有 Embedding，直接載入。")
        return stored_vectors

    print("找不到既有 Embedding，開始建立...")

    for index, chunk in enumerate(chunks, start=1):
        print(f"正在建立 Embedding：{index}/{len(chunks)}")

        chunk["embedding"] = create_embedding(
            chunk["text"]
        )

    save_vectors(chunks, path)

    print("Embedding 建立完成並已儲存。")

    return chunks