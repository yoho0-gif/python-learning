import chromadb
from chromadb.config import Settings


client = chromadb.PersistentClient(path="rag_document_chat/chroma_db")
collection = client.get_or_create_collection(
    name="labor_law_fix", 
    metadata={
        "hnsw:space": "cosine",
        "hnsw:batch_size": 10000
    }
)
def get_count():
    return collection.count()

def add_chunks(chunks, batch_size=10):
    if not chunks:
        print("沒有 Chunk 資料可寫入。")
        return

    ids = []
    documents = []
    embeddings = []

    for index, chunk in enumerate(chunks):
        embedding = chunk.get("embedding")

        if embedding is None or len(embedding) == 0:
            print(f"Chunk {index} 的 Embedding 為空，跳過！")
            continue

        ids.append(f"chunk_{index}_{chunk.get('id', 'x')}")
        documents.append(str(chunk["text"]))
        embeddings.append(chunk["embedding"])

    total = len(ids)
    print(
        f" 準備寫入 ChromaDB：共有 {len(ids)} 筆有效資料，向量維度為 {len(embeddings[0])}"
    )

    for i in range(0, total, batch_size):
        batch_ids = ids[i : i + batch_size]
        batch_docs = documents[i : i + batch_size]
        batch_embs = embeddings[i : i + batch_size]

        try:
            print(f" 正在寫入第 {i + 1} ~ {i + len(batch_ids)} 筆...")
            
            collection.add(
                ids=batch_ids, documents=batch_docs, embeddings=batch_embs
            )
        except Exception as e:
            print(f" 第 {i + 1} 批寫入失敗: {e}")
            return

    print(f" 成功將 {total} 筆高維度 Chunk 完整寫入 ChromaDB！")
        
    
def search(query_embedding, top_k=3):
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results