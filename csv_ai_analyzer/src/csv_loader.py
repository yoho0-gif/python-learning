import csv

def load_csv(path):
    data = []
    try:
        with open(path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
            if not data:
                print("CSV檔案為空，請檢查檔案內容。")
                return None
        return data
    except FileNotFoundError:
        print(f"找不到檔案: {path}")
        return None
    except Exception as e:
        print(f"讀取CSV檔案時發生錯誤: {e}")
        return None

