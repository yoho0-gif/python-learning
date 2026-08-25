from gemini_client import ask_question
from document_loader import load_documents
from text_splitter import split_text, split_text_by_article
from keyword_retriever import retrieve_chunks
from semantic_retriever import retrieve_similar_chunks


def main():
    document_text = load_documents("rag_document_chat/sample/Labor_Standards_Act.pdf")

    if not document_text:
        print("無法讀取內容！")
        return
    
    chunks = split_text_by_article(document_text)
    print(f"總共切出 {len(chunks)} 個條文：\n")

    query = input("請輸入查詢關鍵字：").strip()

    if not query: 
        print("請輸入問題！") 
        return


    results = retrieve_chunks(chunks,query,top_k=3)

    print(f"\n針對'{query}'檢索到的前 {len(results)} 個相關結果：\n")

    if not results:
        print("沒有找到相關的條文。")
        return

    for item in results:
        chunk = item["chunk"]
        score = item["score"]
 
        chunk_id = chunk.get("id", "N/A") if isinstance(chunk, dict) else "N/A"
        text = chunk.get("text", chunk) if isinstance(chunk, dict) else chunk

        print(f"【Chunk ID: {chunk_id} | 相關分數 (Score): {score}】")
        print(text)
        print("-" * 50)

    context = "\n\n".join( item["chunk"]["text"] for item in results )

    print("\n正在請 AI 根據檢索內容回答...\n")
    answer = ask_question(query, context)
    print(f"AI 回答：\n{answer}")


if __name__ == "__main__":
    main()
