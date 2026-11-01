import json
from pathlib import Path

from google import genai
from config import API_KEY


client = genai.Client(api_key=API_KEY)

MODEL_NAME = "gemini-3.5-flash"
DATASET_PATH = Path(__file__).with_name("test_dataset.json")


def evaluate_answer(question, answer, expected_answer):
    """
    使用 LLM 評估 RAG Answer 是否正確回答問題。
    """

    prompt = f"""
你是一個專業的 RAG Evaluation Judge。

請比較「使用者問題」、「標準答案」與「AI 回答」。

【使用者問題】
{question}

【標準答案】
{expected_answer}

【AI 回答】
{answer}

請按照以下標準評分：

1 = 完全錯誤
2 = 大部分錯誤
3 = 部分正確
4 = 大致正確
5 = 完全正確

請只輸出 JSON，不要加入 Markdown：

{{
    "score": 1,
    "reason": "簡短說明評分原因"
}}
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text


def load_test_dataset():
    """
    載入 Evaluation Dataset。
    """

    with DATASET_PATH.open("r", encoding="utf-8") as file:
        return json.load(file)


def main():
    dataset = load_test_dataset()

    for index, item in enumerate(dataset, start=1):

        print("=" * 60)
        print(f"Test Case {index}")

        print("Question:")
        print(item["question"])

        print("\nExpected Answer:")
        print(item["expected_answer"])

        answer = input("\n請輸入 RAG Answer：")

        result = evaluate_answer(
            question=item["question"],
            answer=answer,
            expected_answer=item["expected_answer"]
        )

        print("\nEvaluation Result:")
        print(result)


if __name__ == "__main__":
    main()
