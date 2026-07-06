class GitHubUser:
    def __init__(self, username, name, followers, public_repos):
        self.username = username
        self.name = name
        self.followers = followers
        self.public_repos = public_repos
    def show_info(self):
        print(f"Username: {self.username}")
        print(f"Name: {self.name}")
        print(f"Followers: {self.followers}")
        print(f"Public Repositories: {self.public_repos}")
    def is_popular(self):
        if self.followers > 1000:
            print(f"熱門GitHub用戶")
        else:
            print(f"一般用戶")

user = GitHubUser(
    "torvalds",
    "Linus Torvalds",
    250000,
    8
)
user.show_info()
user.is_popular()