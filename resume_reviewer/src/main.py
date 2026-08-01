from config import API_KEY
from display import show_title, show_subjects
from gemini_client import ask_ai, review_resume
from prompt_templates import RESUME_REVIEWER
from resume_reader import load_resume
from report_writer import save_report

show_title()
show_subjects()
resume_content = None

while True:
    prompt = input("You: ")

    if not prompt.strip():
        print("請輸入問題！")
        continue
    elif prompt.strip().lower() == "exit":
        print("感謝使用！")
        break

    try:
        if prompt.endswith((".txt", ".md")):
            print(f"正在讀取檔案:{prompt}...")
            resume_content = load_resume(prompt)
        elif resume_content is None:
            print("無法讀取履歷內容或內容為空，請重新輸入！\n")
            continue
        else:
            resume_content = prompt
        
        print("AI分析履歷中，請稍後...\n")

        reply = review_resume(resume_content)
        print(f"AI: {reply}\n")
        save_report(reply)
        
    except Exception as e:
        print("AI 回覆失敗")
        print(e)    
