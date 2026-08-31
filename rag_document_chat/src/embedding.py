from google import genai
from google.genai import types
from config import API_KEY
import numpy as np
import time

client = genai.Client(api_key=API_KEY)

def create_embedding(text):
    for attempt in range(3):
        try:
            response = client.models.embed_content(
                model="gemini-embedding-001",
                contents=text,
                config=types.EmbedContentConfig(output_dimensionality=768)
            )
            # 相容最新 google-genai SDK 屬性
            if hasattr(response, "embedding") and response.embedding:
                return response.embedding.values
            elif hasattr(response, "embeddings") and response.embeddings:
                return response.embeddings[0].values
            return None

        except Exception as e:
            error_str = str(e)
            if "429" in error_str or "RESOURCE_EXHAUSTED" in error_str:
                print(
                    f" API 限流 (429)，等待 10 秒後重試 ({attempt + 1}/3)..."
                )
                time.sleep(10)
            else:
                print(f" Embedding 生成失敗: {e}")
                return None
    return None

def cosine_similarity(vector_a, vector_b):
    a = np.array(vector_a)
    b = np.array(vector_b)

    return np.dot(a, b) / (
        np.linalg.norm(a) * np.linalg.norm(b)
    )
