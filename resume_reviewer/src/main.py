from config import API_KEY
from display import show_title, show_subjects
from gemini_client import review_resume
from report_writer import save_report
from document_loader import load_document

show_title()
show_subjects()
resume_content = None


while True:
    prompt = input("請輸入履歷檔案路徑: ").strip()
    resume_content = load_document(prompt)

    if prompt.lower() == "exit":
        print("感謝使用！")
        break

    if resume_content:
        print("\nAI 分析履歷中，請稍後...\n")
        result = review_resume(resume_content)
        
        print(f"AI 回覆內容：\n{result}\n")
        save_report(result)
