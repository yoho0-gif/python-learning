from google import genai
from google.genai import types
from config import API_KEY
from prompt_templates import GITHUB_ANALYZER


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
def analyze_github_profile(summary):
    system_prompt = GITHUB_ANALYZER
    history = [
        {"role": "user", "parts": [{"text": summary}]}
    ]
    return ask_ai(history, system_prompt)
