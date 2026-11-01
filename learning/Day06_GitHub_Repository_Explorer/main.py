# main.py
from display import show_title, show_repositories, show_total_stars
from github_api import get_user

show_title()

username = input("請輸入 GitHub 使用者名稱：")
data = get_user(username)

if data is None:
    print("找不到此使用者或發生錯誤！")
else:   
    total_stars = 0
    for repo in data:
        total_stars += repo["stargazers_count"]
    show_repositories(data)
    show_total_stars(total_stars)