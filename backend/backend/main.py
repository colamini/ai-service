
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from rag_service import get_qa_chain, build_vector_store
import os

app = FastAPI()

origins = ["http://localhost:8080"]  # Vue 默认端口
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    question: str

qa_chain = get_qa_chain()

@app.post("/ask")
def ask_question(query: Query):
    result = qa_chain.run(query.question)
    return {"answer": result}

@app.get("/init")
def initialize():
    build_vector_store()
    return {"status": "Index built"}
