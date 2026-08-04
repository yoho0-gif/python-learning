import json
from github_api import get_repositories
from github_analyzer import summarize_repositories
from gemini_client import analyze_github_profile
from report_writer import save_report


def main():
    username = input("請輸入 GitHub Username: ").strip()
    
    if not username:
        print("請輸入有效的使用者名稱！")
        return

    print(f"\n正在抓取 {username} 的 GitHub 資料...")
    repos = get_repositories(username)

    if not repos:
        print("無法取得資料，請確認使用者名稱是否正確或網路連線是否正常。")
        return
    
    print("正在分析與整理資料...\n")
    summary = summarize_repositories(repos)

    if not summary:
        print("無法分析資料，請確認使用者是否有公開的專案。")
        return

    print("=== 統計結果 Summary ===")
    print(f"專案總數: {summary['repo_count']}")
    print(f"獲得 Star 總數: {summary['total_stars']}")
    print("\n使用的程式語言統計:")

    for lang, count in summary['top_languages'].items():
        print(f"  - {lang}: {count} 個專案")

    if summary['most_starred_repo']:
        top = summary['most_starred_repo']
        print(f"\n 最受歡迎的專案: {top['name']} ({top['stars']} stars)")
        print(f"  簡介: {top['description']}")

    summary_json = json.dumps(summary, indent=2, ensure_ascii=False)
    ai_analysis = analyze_github_profile(str(summary_json))
    print("\n=== AI 分析結果 ===")
    print(ai_analysis)
    save_report(ai_analysis)


if __name__ == "__main__":
    main()  