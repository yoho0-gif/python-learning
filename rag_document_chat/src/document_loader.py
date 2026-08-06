import os
from pypdf import PdfReader

def load_pdf(path):
    if not os.path.exists(path):
        print(f"錯誤：找不到 PDF 檔案 '{path}'")
        return None

    try:
        reader = PdfReader(path)
        extracted_text = []
        total_pages = len(reader.pages)

        for index, page in enumerate(reader.pages, start=1):
            print(f"正在讀取第 {index}/{total_pages} 頁...")
            
            text = page.extract_text()
            if text:
                extracted_text.append(text)

        full_text = "\n".join(extracted_text).strip()

        if not full_text:
            print(f"警告：無法從 '{path}' 擷取文字（可能是圖片或掃描檔 PDF）")
            return None
        return full_text

    except Exception as e:
        print(f"讀取 PDF 時發生錯誤: {e}")
        return None


def load_txt(path):
    try:
        with open(path, 'r', encoding="utf-8") as file:
            resume_content = file.read()
            if not resume_content.strip():
                print(f"警告：檔案 '{path}' 內容為空")
                return None
        return resume_content
    except FileNotFoundError:
        print(f"找不到檔案: {path}")
        return None
    except Exception as e:
        print(f"讀取檔案時發生錯誤: {e}")
        return None


def load_document(path):
    if not os.path.exists(path):
        print(f"錯誤：找不到檔案 '{path}'")
        return None

    _, ext = os.path.splitext(path)
    ext = ext.lower()

    if ext in ['.txt', '.md']:
        print(f"偵測到純文字檔案，使用 txt/md 讀取器...")
        return load_txt(path)
    elif ext == '.pdf':
        print(f"偵測到 PDF 檔案，使用 PDF 解析器...")
        return load_pdf(path)
    else:
        print(f"不支援的檔案格式：'{ext}'（僅支援 .txt, .md, .pdf）")
        return None

load_document("rag_document_chat/sample/Labor_Standards_Act.pdf")