from document_loader import load_documents
from text_splitter import split_text

def main():
    document_text = load_documents("rag_document_chat/sample/Labor_Standards_Act.pdf")

    if not document_text:
        print("無法讀取內容！")
        return
    # Split each document into paragraphs

    chunks = split_text(document_text)
    print(f"總共切出 {len(chunks)} 個段落：\n")
    for i, chunk in enumerate(chunks, start=1):
        print(f"【Chunk {i}】")
        print(f"{chunk}")
        print("-" * 40)
    # for doc in document_text:
    #     paragraphs = split_text(doc)
    #     print(f"Document: {doc[:30]}...")  # Print the first 30 characters of the document
    #     for i, paragraph in enumerate(paragraphs):
    #         print(f"Paragraph {i + 1}: {paragraph[:50]}...")  # Print the first 50 characters of each paragraph
    #     print("\n" + "="*40 + "\n")

if __name__ == "__main__":
    main()
