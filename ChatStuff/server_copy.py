import asyncio
# import ollama

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from contextlib import asynccontextmanager

from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader, WebBaseLoader, TextLoader
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
async def lifespan(app: FastAPI):
    print("starting system ...")
    app.state.llm = OllamaLLM(model="gemma3:1b", temperature=0.3)
    app.state.embeddings = OllamaEmbeddings(model="nomic-embed-text")

    docs = []
    docs += DirectoryLoader("../data", glob="**/*.pdf", loader_cls=PyPDFLoader).load()
    docs += DirectoryLoader("../data", glob="**/*.txt", loader_cls=TextLoader).load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)

    vectorstore = InMemoryVectorStore(app.state.embeddings)
    await vectorstore.aadd_documents(chunks)
    app.state.vectorstore = vectorstore

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
    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
                You are an assistant that answers questions from the given data.
                Context: {context}
                Question: {request.message}
                Answer:
                """

    response = await llm.ainvoke(prompt)

    return {"reply": response}
