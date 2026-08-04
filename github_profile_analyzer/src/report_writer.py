def save_report(content):
    with open("github_analysis.md", "w", encoding="utf-8") as file:
        file.write(content)