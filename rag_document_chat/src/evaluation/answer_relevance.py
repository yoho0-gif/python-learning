
import json

from pydantic import BaseModel, Field
from google import genai
from google.genai import types

from src.config import API_KEY


client = genai.Client(api_key=API_KEY)

# 請使用你目前環境支援的 Gemini 模型名稱。
MODEL_NAME = "gemini-3.6-flash"


class RelevanceResult(BaseModel):
    score: int = Field(ge=1, le=5)
    is_relevant: bool
    reason: str


def evaluate_answer_relevance(
    question: str,
    answer: str,
) -> dict:
    """
    評估答案是否切合使用者問題。

    1 分：完全離題
    2 分：只有少量相關內容
    3 分：部分回答問題
    4 分：大致切題
    5 分：直接且完整地回應問題
    """

    prompt = f"""
你是專業的 AI Answer Relevance Evaluator。

你的任務是判斷 AI 的答案是否回應使用者的問題。

評分標準：
1：完全離題，沒有回答問題。
2：只有少量相關內容，主要沒有回答問題。
3：部分回答問題，但有明顯遺漏。
4：大致回答問題，只有少量遺漏。
5：直接且完整地回應問題。

注意：
- 不要因為答案很長就給高分。
- 不要因為答案提到相同關鍵字就認定相關。
- 只評估問題與答案的相關性，不要將事實正確性混入評分。
- is_relevant 在 score >= 4 時為 true，否則為 false。

使用者問題：
{question}

AI 的答案：
{answer}
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=RelevanceResult,
            temperature=0,
        ),
    )

    if not response.text:
        raise ValueError("Evaluation 模型沒有回傳結果。")

    result = RelevanceResult.model_validate_json(response.text)

    return result.model_dump()


def main():
    test_cases = [
        {
            "question": "FAISS 是用來做什麼的？",
            "answer": (
                "FAISS 是用來進行向量相似度搜尋的函式庫，"
                "可以協助快速找到相似的向量。"
            ),
        },
        {
            "question": "FAISS 是用來做什麼的？",
            "answer": "FAISS 是一個 AI 工具。",
        },
        {
            "question": "FAISS 是用來做什麼的？",
            "answer": "Python 是一種高階程式語言。",
        },
    ]

    for index, item in enumerate(test_cases, start=1):
        print(f"\n{'=' * 50}")
        print(f"Test Case {index}")
        print("Question:", item["question"])
        print("Answer:", item["answer"])

        result = evaluate_answer_relevance(
            question=item["question"],
            answer=item["answer"],
        )

        print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
