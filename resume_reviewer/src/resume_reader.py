def load_resume(path):
    try:
        with open(path, 'r', encoding="utf-8") as file:
            resume_content = file.read()
        return resume_content
    except FileNotFoundError:
        print(f"找不到檔案: {path}")
        return None
    except Exception as e:
        print(f"讀取檔案時發生錯誤: {e}")
        return None