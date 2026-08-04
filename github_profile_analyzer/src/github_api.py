import requests

# torvalds
def get_repositories(username):
    url = f"https://api.github.com/users/{username}/repos"
    headers = {
    "Accept": "application/vnd.github+json"
}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            print(f"查無使用者'{username}'")
            return None
        else:
            print(f"無法取得使用者 '{username}' 的資料，HTTP 狀態碼: {response.status_code}")
            return None
    except requests.exceptions.Timeout:
        print("請求逾時，請檢查網路連線或稍後再試。")
        return None
    except Exception as e:
        print(f"發生錯誤: {e}")
        return None

