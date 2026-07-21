from config import API_KEY
from display import show_title
from gemini_client import ask_ai

show_title()
print(API_KEY)
while True:
    prompt = input("You: ")

    if not prompt.strip():
        print("請輸入問題！")
        continue
        
    if prompt.strip().lower() == "exit":
        print("感謝使用！")
        break
    try:
        reply = ask_ai(prompt)
        print(f"AI: {reply}\n")
    except Exception as e:
        print("AI 回覆失敗")
        print(e)    
