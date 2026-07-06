def show_title():
    print("=" * 25 + "\n")
    print("GitHub User Information\n")
    print("=" * 25 + "\n")
def show_total_stars(total_stars):
    print(f"Total Stars\n\n{total_stars}")
def show_repository(repo):
    if repo["stargazers_count"] > 1000:
            print(repo["name"] + "\n")
            if repo["language"] is None:
                print(f"language: Unknown\n")
            else:
                print(f"language: {repo['language']}\n")
            print(f"stargazers: {repo['stargazers_count']}\n")
            print("-" * 25 + "\n")

def show_repositories(repos):
    for repo in repos:
         show_repository(repo)
    