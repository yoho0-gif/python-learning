from google import genai
from config import API_KEY

client = genai.Client(api_key=API_KEY)

def ask_ai(prompt):
    response = client.models.generate_content(
        model="gemini-3.5-flash", contents=prompt
    )
    return response.text

