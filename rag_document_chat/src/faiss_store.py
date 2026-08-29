# 新建或直接蓋掉 chroma_store.py 內容
import faiss
import numpy as np
import json
import os

INDEX_PATH = "rag_document_chat/faiss_index.bin"
TEXTS_PATH = "rag_document_chat/faiss_texts.json"

# 建立一個全局的列表來存文字
stored_texts = []

def add_chunks(chunks):
    global stored_texts
    if not chunks: return

    embeddings = [c["embedding"] for c in chunks if c.get("embedding")]
    stored_texts = [c["text"] for c in chunks if c.get("embedding")]

    # 轉成 numpy float32 矩陣
    embedding_matrix = np.array(embeddings).astype('float32')
    dimension = embedding_matrix.shape[1]

    # 建立 FAISS 內積（Cosine 相似度需先做 L2 正規化，或用 IndexFlatIP）
    # 為了方便，我們直接使用基礎的 L2 距離索引
    index = faiss.IndexFlatL2(dimension)
    index.add(embedding_matrix)

    # 儲存到硬碟
    faiss.write_index(index, INDEX_PATH)
    with open(TEXTS_PATH, "w", encoding="utf-8") as f:
        json.dump(stored_texts, f, ensure_ascii=False)
    print(f" 成功將 {len(stored_texts)} 筆向量安全存入 FAISS 資料庫！")

def search(query_embedding, top_k=3):
    # 載入資料庫
    index = faiss.read_index(INDEX_PATH)
    with open(TEXTS_PATH, "r", encoding="utf-8") as f:
        stored_texts = json.load(f)

    query_arr = np.array([query_embedding]).astype('float32')
    distances, indices = index.search(query_arr, top_k)

    # 包裝成與原本 main.py 相容的 Chroma 回傳格式
    results = {
        "documents": [[stored_texts[idx] for idx in indices[0] if idx != -1]],
        "ids": [[f"chunk_{idx}" for idx in indices[0] if idx != -1]],
        "distances": [distances[0].tolist()]
    }
    return results
