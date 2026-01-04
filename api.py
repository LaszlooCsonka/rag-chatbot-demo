import os
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain.chains import RetrievalQA

# 1. Loading environment variables
load_dotenv()

app = FastAPI(
    title="RAG Knowledge API", 
    description="REST API endpoint for document-based Question Answering"
)

# 2. Initializing RAG engine (Using same logic as in app.py)
loader = TextLoader("data.txt", encoding="utf-8")
documents = loader.load()
vectorstore = FAISS.from_documents(documents, OpenAIEmbeddings())
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
qa_chain = RetrievalQA.from_chain_type(
    llm=llm, 
    chain_type="stuff", 
    retriever=vectorstore.as_retriever()
)

# 3. Data Model for API Requests
class ChatRequest(BaseModel):
    query: str

# 4. API Endpoints
@app.get("/")
def read_root():
    return {"status": "API is online", "service": "RAG-Core-Service"}

@app.post("/ask")
def ask_question(request: ChatRequest):
    response = qa_chain.invoke(request.query)
    return {"answer": response["result"]}