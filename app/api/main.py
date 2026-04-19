from fastapi import FastAPI
from pydantic import BaseModel, Field

from app.services.orchestrator import answer_query

app = FastAPI(title="Ethiopian Bible Guardian API")


class ChatRequest(BaseModel):
    query: str = Field(min_length=1)
    top_k: int = Field(default=5, ge=1, le=20)


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/chat")
def chat(req: ChatRequest) -> dict:
    return answer_query(query=req.query, top_k=req.top_k)
