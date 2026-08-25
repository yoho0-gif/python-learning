from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
if API_KEY is None:
    raise ValueError("找不到 GEMINI_API_KEY")
