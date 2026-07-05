from github_api import get_user
from display import show_title, show_user

show_title()
username = input("請輸入 GitHub 使用者：")
data = get_user(username)
if data is None:
    print("找不到該使用者")
else:
    show_user(data)