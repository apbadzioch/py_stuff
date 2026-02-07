import asyncio
# import ollama

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from contextlib import asynccontextmanager

from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader, WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
# from langchain_community.vectorstores import FAISS

origins = [
    "http://localhost:8000",
    "https://www.onebadev.com",
]

class ChatRequest(BaseModel):
    message: str

@asynccontextmanager
async def lifespan(app:FastAPI):
    print("starting system ...")
    app.state.llm = OllamaLLM(model="gemma3:1b", temperature=0.3)
    app.state.embeddings = OllamaEmbeddings(model="nomic-embed-text")

    docs = []
    docs += DirectoryLoader("info", glob="**/*.pdf", loader_cls=PyPDFLoader).load()
    docs += DirectoryLoader('info')

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)

    app.state.vectorstore = InMemoryVectorStore(chunks, app.state.embeddings)

    print("system loaded")
    yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
@app.post('/api/chat')
async def chat(request: ChatRequest):
    llm = app.state.llm
    vs = app.state.vectorstore

    docs = vs.similarity_search(request.message, k=3)
    response = llm.invoke(...)

    return {"reply": response}
