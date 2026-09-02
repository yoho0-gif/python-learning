from google import genai
from google.genai import types
from config import API_KEY
from prompt_templates import RAG_PROMPT


client = genai.Client(api_key=API_KEY)

def ask_ai(history, system_prompt):
    response = client.models.generate_content(
        model="gemini-3.5-flash", 
        contents=history,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt
        )
    )
    return response.text

def ask_question(question, context_text, conversation_history=None):
    history = [
        {"role": "user", "parts": [{"text": context_text}]},
        {"role": "user", "parts": [{"text": question}]}
    ]

    if conversation_history is None:
        conversation_history = []

    history = []

    for message in conversation_history:
        
        history.append({
            "role": message["role"],
            "parts": [{"text": message["text"]}]})


    history.append({
        "role": "user",
        "parts": [{"text": f"""以下是從文件檢索到的相關內容：{context_text}請根據以上文件內容回答使用者問題。"""}]})


    history.append({"role": "user", 
                    "parts": [{"text": question}]})

    return ask_ai(
        history,
        RAG_PROMPT
    )
