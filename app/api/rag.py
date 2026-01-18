from fastapi import APIRouter

router = APIRouter(prefix="/api/rag", tags=["rag"])

@router.post("/query")
def query_rag(question: str):
    # TODO: Implement RAG pipeline
    return {
        "answer": "RAG pipeline not yet implemented",
        "sources": []
    }
