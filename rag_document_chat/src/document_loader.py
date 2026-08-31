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
            print(
                f"正在讀取第 "
                f"{index}/{total_pages} 頁..."
            )
            text = page.extract_text()
            if text:
                extracted_text.append(text)
        full_text = "\n".join(extracted_text).strip()

        if not full_text:
            print(f"警告：無法從 '{path}' 擷取文字")
            return None
        return full_text

    except Exception as e:
        print(f"讀取 PDF 時發生錯誤: {e}")
        return None


def load_txt(path):
    try:
        with open(path, 'r', encoding="utf-8") as file:
            content = file.read()
            if not content.strip():
                print(f"警告：檔案 '{path}' 內容為空")
                return None
        return content
    except FileNotFoundError:
        print(f"找不到檔案: {path}")
        return None
    except Exception as e:
        print(f"讀取檔案時發生錯誤: {e}")
        return None


def load_documents(path):
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

def load_documents_from_folder(folder_path):

    if not os.path.exists(folder_path):
        print(
            f"找不到資料夾：{folder_path}"
        )
        return []

    documents = []

    for filename in os.listdir(folder_path):

        path = os.path.join(
            folder_path,
            filename
        )

        if not os.path.isfile(path):
            continue

        _, ext = os.path.splitext(filename)
        ext = ext.lower()

        if ext not in [".pdf", ".txt", ".md"]:
            continue

        print("\n" + "=" * 50)
        print(f"正在讀取文件：{filename}")
        print("=" * 50)

        text = load_documents(path)

        if text:
            documents.append({
                "source": filename,
                "text": text
            })

    return documents