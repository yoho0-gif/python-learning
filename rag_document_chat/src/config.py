from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv(Path(__file__).with_name(".env"))

API_KEY = os.getenv("GEMINI_API_KEY")
if API_KEY is None:
    raise ValueError("找不到 GEMINI_API_KEY")
