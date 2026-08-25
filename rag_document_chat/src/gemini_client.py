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
def ask_question(question, context_text):
    system_prompt = RAG_PROMPT
    history = [
        {"role": "user", "parts": [{"text": context_text}]},
        {"role": "user", "parts": [{"text": question}]}
    ]
    return ask_ai(history, system_prompt)

