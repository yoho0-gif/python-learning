from config import API_KEY
from display import show_title, show_prompt
from gemini_client import ask_ai
from history import add_user_message, add_ai_message, get_history, clear_history
from prompt_templates import PYTHON_TEACHER, ENGLISH_TEACHER, RESUME_ADVISOR, INTERVIEWER

show_title()
show_prompt()

choice = input("請輸入選項: ").strip()
if choice == "1":
    current_system_prompt = PYTHON_TEACHER
    print("你已選擇 Python 講師模式")
elif choice == "2":
    current_system_prompt = ENGLISH_TEACHER
    print("你已選擇 英文老師模式")
elif choice == "3":
    current_system_prompt = RESUME_ADVISOR
    print("你已選擇 履歷顧問模式")
elif choice == "4":
    current_system_prompt = INTERVIEWER
    print("你已選擇 面試官模式")

while True:
    prompt = input("You: ")

    if not prompt.strip():
        print("請輸入問題！")
        continue
    elif prompt.strip().lower() == "exit":
        print("感謝使用！")
        break
    elif prompt.strip().lower() == "clear":
        clear_history()
        print("歷史紀錄已清除！")
        continue
    elif prompt.strip().lower() == "/help":
        print(current_system_prompt)
    elif prompt.strip().lower() == "/switch":
        show_prompt()
        choice = input("請輸入選項: ").strip()
        if choice == "1":
            current_system_prompt = PYTHON_TEACHER
            print("你已切換到 Python 講師模式")
        elif choice == "2":
            current_system_prompt = ENGLISH_TEACHER
            print("你已切換到 英文老師模式")
        elif choice == "3":
            current_system_prompt = RESUME_ADVISOR
            print("你已切換到 履歷顧問模式")
        elif choice == "4":
            current_system_prompt = INTERVIEWER
            print("你已切換到 面試官模式")
        continue
        

    try:
        add_user_message(prompt)
        reply = ask_ai(get_history(), current_system_prompt)
        add_ai_message(reply)
        print(f"AI: {reply}\n")
        
    except Exception as e:
        print("AI 回覆失敗")
        print(e)    
