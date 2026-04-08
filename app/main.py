from fastapi import FastAPI
from app.models.request import QueryRequest
from app.services.orchestrator import process_query

app = FastAPI()

@app.post("/chat")
async def chat(req: QueryRequest):
    return {"response": process_query(req.message)}