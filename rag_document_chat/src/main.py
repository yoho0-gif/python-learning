from document_loader import load_documents_from_folder
from incremental_indexer import update_index
from embedding import create_embedding
from faiss_store import search, load_store
from gemini_client import ask_question
from conversation import add_user_message, add_ai_message, get_recent_history, clear_history

DOCUMENT_FOLDER = ("rag_document_chat/documents")

def main():

    print("=" * 60)
    print("Multi-Document RAG")
    print("=" * 60)
    documents = load_documents_from_folder(DOCUMENT_FOLDER)

    if not documents:
        print("沒有找到任何文件！")
        return

    print(f"\n目前共有 {len(documents)} 份文件")
    print("\n=== 檢查文件變更 ===")
    
    update_index(documents)
    store = load_store()

    if store is None:

        print("FAISS Index 建立失敗！")
        return

    print("\nRAG Chat 已啟動")
    print("輸入 exit 離開")
    print("輸入 clear 清除對話")
    print("-" * 50)

    index, chunks = store
    while True:

        query = input("\nYou: ").strip()

        if not query:
            print("請輸入問題！")
            continue

        if query.lower() == "exit":

            print("感謝使用！")
            break

        if query.lower() == "clear":

            clear_history()

            print("對話紀錄已清除！")
            continue

        query_embedding = create_embedding(query)

        if query_embedding is None:

            print("無法建立問題 Embedding！")
            continue

        results = search(index, chunks, query_embedding, top_k=3)

        if not results:

            print("沒有找到相關內容！")
            continue
        
        context_parts = []

        print("\n=== 找到相關文件 ===")

        for item in results:
            chunk = item["chunk"]
            distance = item["distance"]
            print(f"\n來源：{chunk['source']}")
            print(f"Distance: {distance:.4f}")

            context_parts.append(f"""來源：{chunk['source']}{chunk['text']}""")
            
        context = "\n\n".join(context_parts)
        recent_history = get_recent_history(limit=6)
        answer = ask_question(query, context, recent_history)

        print("\n=== AI 回答 ===")
        print(answer)

        add_user_message(query)
        add_ai_message(answer)


if __name__ == "__main__":
    main()