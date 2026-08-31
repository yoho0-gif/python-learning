from document_loader import load_documents
from text_splitter import split_text_by_article
from embedding import create_embedding
from faiss_store import add_chunks, search, load_store
from gemini_client import ask_question


def main():
    document_text = load_documents(
        "rag_document_chat/sample/Labor_Standards_Act.pdf"
    )

    if not document_text:
        print("無法讀取內容！")
        return

    source = "Labor_Standards_Act.pdf"

    chunks = split_text_by_article(
    document_text,
    source=source
    )
    store = load_store()

    if store is None:

        print("\n找不到既有 Vector Store")
        print("開始建立 Embedding...\n")

        for index, chunk in enumerate(
            chunks,
            start=1
        ):

            print(
                f"正在建立 Embedding："
                f"{index}/{len(chunks)}"
            )

            embedding = create_embedding(
                chunk["text"]
            )

            if embedding is not None:
                chunk["embedding"] = embedding
    
        add_chunks(chunks)

        store = load_store()
    else:
            print("\n找到既有 Vector Store")

    index, stored_chunks = store

    query = input("請輸入問題：").strip()
    
    if not query:
        print("請輸入問題！")
        return
    
    query_embedding = create_embedding(query)    
    if query_embedding is None:
        print("無法建立問題的 Embedding！")
        return
    
    results = search(
        index,
        stored_chunks,
        query_embedding,
        top_k=3
    )
    
    print("\n=== Vector Search 結果 ===")

    for result in results:

        chunk = result["chunk"]
        distance = result["distance"]

        print(f"\n【{chunk['article']}】")
        print(f"來源：{chunk['source']}")
        print(f"Distance: {distance:.4f}")
        print(chunk["text"])
        print("-" * 50)

    context_parts = []

    for result in results:
        chunk = result["chunk"]
        context_parts.append(f"""來源：{chunk['source']}條文：{chunk['article']}{chunk['text']}""")

    context = "\n\n".join(context_parts)
    answer = ask_question(query,context)

    print("\n=== AI 回答 ===")
    print(answer)


if __name__ == "__main__":
    main()