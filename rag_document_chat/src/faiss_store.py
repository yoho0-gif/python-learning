import faiss
import numpy as np
import json
import os

INDEX_PATH = "rag_document_chat/faiss_index.bin"
TEXTS_PATH = "rag_document_chat/faiss_texts.json"

stored_texts = []

def add_chunks(chunks):
    valid_chunks = [
        chunk
        for chunk in chunks
        if chunk.get("embedding") is not None
    ]
    if not valid_chunks:
        print("沒有可以儲存的 Chunk")
        return
    
    embeddings = [chunk["embedding"] for chunk in valid_chunks]
    embedding_matrix = np.array(embeddings,dtype="float32")
    dimension = embedding_matrix.shape[1]

    # 建立 FAISS 內積（Cosine 相似度需先做 L2 正規化，或用 IndexFlatIP）
    # 為了方便，我們直接使用基礎的 L2 距離索引
    index = faiss.IndexFlatL2(dimension)
    index.add(embedding_matrix)

    faiss.write_index(index, INDEX_PATH)

    with open(TEXTS_PATH, "w", encoding="utf-8") as file:
        json.dump(valid_chunks, file, ensure_ascii=False, indent=2)
    print(f"成功儲存 {len(valid_chunks)} 個 Chunk")

def load_store():
    if not os.path.exists(INDEX_PATH):
        return None
    if not os.path.exists(TEXTS_PATH):
        return None

    index = faiss.read_index(
        INDEX_PATH
    )

    with open(
        TEXTS_PATH,
        "r",
        encoding="utf-8"
    ) as file:

        chunks = json.load(file)

    return index, chunks

def search(index, chunks, query_embedding, top_k=3):
    if index is None or not chunks:
        print("FAISS Index 或 Chunk 資料不存在")
        return {
            "documents": [[]],
            "ids": [[]],
            "distances": [[]]
        }
    query_arr = np.array([query_embedding], dtype="float32")
    top_k = min(top_k,len(chunks))
    distances, indices = index.search(query_arr, top_k)

    documents = []
    ids = []
    valid_distances = []

    for dix, distance in zip(indices[0], distances[0]):
        if dix != -1:
            chunk = chunks[dix]
            documents.append(chunk["text"])
            ids.append(chunk["id"])
            valid_distances.append(float(distance))

    return {
        "documents": [documents],
        "ids": [ids],
        "distances": [valid_distances]
    }