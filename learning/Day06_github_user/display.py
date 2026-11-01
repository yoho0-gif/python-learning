def show_title():
    print("=" * 25)
    print("GitHub User Information")
    print("=" * 25)

def show_user(data):
    print(f"使用者: {data['login']}")
    print(f"姓名: {data.get('name', 'N/A')}")
    print(f"公開 Repo: {data['public_repos']}")
    print(f"Followers: {data['followers']}")
    print(f"Following: {data['following']}")
    print(f"建立時間: {data['created_at']}")
    