import requests
# torvalds
username = input("請輸入 GitHub 使用者：")
url = f"https://api.github.com/users/{username}"
response = requests.get(url)
data = response.json()
title = "GitHub User Information"
print("=" * 22)
print(f"{title:^22}")
print("=" * 22 + "\n")

if response.status_code == 404:
    print("查無此使用者")
else:
    print(f"使用者:{data['login']}",f"姓名:{data['name']}",f"公開 Repo:{data['public_repos']}",f"Followers:{data['followers']}",f"Following:{data['following']}",f"建立時間:{data['created_at']}",sep="\n")

