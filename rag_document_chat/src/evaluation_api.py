
from typing import Any

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from evaluation.answer_relevance import (
    evaluate_answer_relevance,
)
from evaluation.faithfulness import (
    evaluate_faithfulness,
)
from evaluation.context_relevance import (
    evaluate_retrieved_contexts,
)
from evaluation.citation_evaluation import (
    evaluate_citation_validity,
)


app = FastAPI(
    title="RAG Evaluation API",
    description="Evaluate relevance, faithfulness and citations.",
    version="1.0.0",
)


# ---------- Request Models ----------

class RelevanceRequest(BaseModel):
    question: str
    answer: str


class FaithfulnessRequest(BaseModel):
    question: str
    context: str
    answer: str


class ContextRequest(BaseModel):
    question: str
    contexts: list[str] = Field(min_length=1)


class Source(BaseModel):
    source_id: str
    text: str


class AnswerClaim(BaseModel):
    claim: str
    citation_ids: list[str] = Field(default_factory=list)


class CitationRequest(BaseModel):
    answer_claims: list[AnswerClaim]
    retrieved_sources: list[Source]


# ---------- Health Check ----------

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "RAG Evaluation API",
    }


# ---------- Answer Relevance ----------

@app.post("/evaluate/relevance")
def evaluate_relevance(request: RelevanceRequest):
    try:
        result = evaluate_answer_relevance(
            question=request.question,
            answer=request.answer,
        )
        return result

    except Exception as exc:
        raise HTTPException(
            status_code=503,
            detail="Relevance evaluation service unavailable.",
        ) from exc


# ---------- Faithfulness ----------

@app.post("/evaluate/faithfulness")
def evaluate_faithfulness_api(
    request: FaithfulnessRequest,
):
    try:
        return evaluate_faithfulness(
            question=request.question,
            context=request.context,
            answer=request.answer,
        )

    except Exception as exc:
        raise HTTPException(
            status_code=503,
            detail="Faithfulness evaluation service unavailable.",
        ) from exc


# ---------- Context Relevance ----------

@app.post("/evaluate/context")
def evaluate_context_api(request: ContextRequest):
    try:
        return evaluate_retrieved_contexts(
            question=request.question,
            contexts=request.contexts,
        )

    except Exception as exc:
        raise HTTPException(
            status_code=503,
            detail="Context evaluation service unavailable.",
        ) from exc


# ---------- Citation Validity ----------

@app.post("/evaluate/citation")
def evaluate_citation_api(request: CitationRequest):
    answer_claims = [
        item.model_dump()
        for item in request.answer_claims
    ]

    retrieved_sources = [
        item.model_dump()
        for item in request.retrieved_sources
    ]

    return evaluate_citation_validity(
        answer_claims=answer_claims,
        retrieved_sources=retrieved_sources,
    )
