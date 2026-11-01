
def evaluate_citation_validity(
    answer_claims: list[dict],
    retrieved_sources: list[dict],
) -> dict:
    """
    檢查答案引用的來源是否存在於本次檢索結果。

    注意：這裡只檢查來源有效性，
    不代表來源內容一定支持答案。
    """

    valid_source_ids = {
        source["source_id"]
        for source in retrieved_sources
    }

    results = []

    for item in answer_claims:
        citation_ids = item.get("citation_ids", [])

        valid_citations = [
            source_id
            for source_id in citation_ids
            if source_id in valid_source_ids
        ]

        invalid_citations = [
            source_id
            for source_id in citation_ids
            if source_id not in valid_source_ids
        ]

        # 沒有引用時，不可以視為通過。
        if not citation_ids:
            status = "missing"
        elif invalid_citations:
            status = "invalid"
        else:
            status = "valid"

        results.append({
            "claim": item["claim"],
            "citation_ids": citation_ids,
            "valid_citations": valid_citations,
            "invalid_citations": invalid_citations,
            "status": status,
        })

    total = len(results)
    valid_count = sum(
        item["status"] == "valid"
        for item in results
    )

    return {
        "total_claims": total,
        "valid_claims": valid_count,
        "citation_validity_score": (
            round(valid_count / total, 3)
            if total else None
        ),
        "results": results,
    }


def main():
    retrieved_sources = [
        {
            "source_id": "source_01",
            "text": (
                "公司提供的年假為 7 天，"
                "適用於到職滿一年的員工。"
            ),
        },
        {
            "source_id": "source_02",
            "text": "公司提供員工教育訓練。",
        },
    ]

    answer_claims = [
        {
            "claim": "到職滿一年的員工有 7 天年假。",
            "citation_ids": ["source_01"],
        },
        {
            "claim": "年假可以折算成現金。",
            "citation_ids": ["source_99"],
        },
        {
            "claim": "公司提供員工教育訓練。",
            "citation_ids": [],
        },
    ]

    result = evaluate_citation_validity(
        answer_claims=answer_claims,
        retrieved_sources=retrieved_sources,
    )

    import json
    print(json.dumps(
        result,
        ensure_ascii=False,
        indent=2,
    ))


if __name__ == "__main__":
    main()
