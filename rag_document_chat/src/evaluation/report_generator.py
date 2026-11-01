
import json
from datetime import datetime
from pathlib import Path
from statistics import mean


def calculate_summary(results: list[dict]) -> dict:
    """統計批次評估結果。"""

    metric_names = [
        "answer_relevance",
        "faithfulness",
        "context_relevance",
        "citation_validity",
    ]

    summary = {
        "total_cases": len(results),
        "metrics": {},
    }

    for metric in metric_names:
        scores = []

        for item in results:
            score = item.get(metric)

            # 只統計數字，排除 None、字串與布林值
            if isinstance(score, (int, float)) and not isinstance(score, bool):
                scores.append(float(score))

        summary["metrics"][metric] = {
            "evaluated_cases": len(scores),
            "average_score": round(mean(scores), 3) if scores else None,
        }

    return summary


def generate_markdown_report(
    results: list[dict],
    summary: dict,
) -> str:
    """將評估結果轉成 Markdown 報告。"""

    lines = [
        "# RAG Evaluation Report",
        "",
        f"- 評估時間：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"- 測試案例數：{summary['total_cases']}",
        "",
        "## 評估指標總覽",
        "",
        "| 指標 | 有效案例數 | 平均分數 |",
        "|---|---:|---:|",
    ]

    metric_labels = {
        "answer_relevance": "回答相關性",
        "faithfulness": "回答忠實度",
        "context_relevance": "檢索內容相關性",
        "citation_validity": "引用有效性",
    }

    for metric, label in metric_labels.items():
        data = summary["metrics"][metric]
        score = data["average_score"]
        score_text = f"{score:.3f}" if score is not None else "N/A"

        lines.append(
            f"| {label} | {data['evaluated_cases']} | {score_text} |"
        )

    lines.extend([
        "",
        "## 個別案例",
        "",
    ])

    for index, item in enumerate(results, start=1):
        question = item.get("question", "未提供問題")

        lines.extend([
            f"### 案例 {index}",
            "",
            f"- 問題：{question}",
        ])

        for metric, label in metric_labels.items():
            score = item.get(metric)
            score_text = str(score) if score is not None else "N/A"
            lines.append(f"- {label}：{score_text}")

        error = item.get("error")
        if error:
            lines.append(f"- 錯誤：{error}")

        lines.append("")

    return "\n".join(lines)


def save_evaluation_report(
    results: list[dict],
    output_dir: str = "evaluation/reports",
) -> dict:
    """輸出 JSON 原始結果與 Markdown 報告。"""

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    summary = calculate_summary(results)

    payload = {
        "summary": summary,
        "results": results,
    }

    json_path = output_path / "evaluation_results.json"
    markdown_path = output_path / "evaluation_report.md"

    json_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    markdown_path.write_text(
        generate_markdown_report(results, summary),
        encoding="utf-8",
    )

    return {
        "summary": summary,
        "json_path": str(json_path),
        "markdown_path": str(markdown_path),
    }


if __name__ == "__main__":
    # 先用模擬資料測試報告功能，不呼叫 Gemini
    demo_results = [
        {
            "question": "勞工正常工作時間一天最多幾小時？",
            "answer_relevance": 5,
            "faithfulness": 1.0,
            "context_relevance": 0.9,
            "citation_validity": 1.0,
        },
        {
            "question": "勞工一週正常工作時間最多幾小時？",
            "answer_relevance": 4,
            "faithfulness": 0.8,
            "context_relevance": 0.7,
            "citation_validity": 0.5,
        },
        {
            "question": "超出正常工時如何處理？",
            "answer_relevance": None,
            "faithfulness": None,
            "context_relevance": None,
            "citation_validity": 0.0,
            "error": "尚未執行模型評估",
        },
    ]

    report = save_evaluation_report(demo_results)

    print("評估報告產生完成！")
    print(json.dumps(report["summary"], ensure_ascii=False, indent=2))
    print(f"\nJSON 結果：{report['json_path']}")
    print(f"Markdown 報告：{report['markdown_path']}")
