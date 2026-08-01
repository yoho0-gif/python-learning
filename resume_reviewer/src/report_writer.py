def save_report(content):
    with open("review_result.md", "w", encoding="utf-8") as file:
        file.write(content)