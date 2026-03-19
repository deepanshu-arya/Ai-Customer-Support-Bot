from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from typing import List
import os

# -------------------------------
# LangChain (latest structure)
# -------------------------------
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import FakeEmbeddings
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate

# -------------------------------
# ⚡ Simple FREE LLM
# -------------------------------

def simple_llm(context: str, question: str) -> str:
    return f"Based on your documents:\n\n{context[:1000]}\n\nAnswer: This is a demo AI response to: {question}"

# -------------------------------
# 🚀 FastAPI App
# -------------------------------

app = FastAPI(title="AI Customer Support Bot")

VECTOR_DB = None


# -------------------------------
# 📄 Upload Document API
# -------------------------------

@app.post("/upload-doc")
async def upload_doc(file: UploadFile = File(...)):
    global VECTOR_DB

    content = await file.read()
    text = content.decode(errors="ignore")

    # Split text into chunks
    splitter = CharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = splitter.split_text(text)

    documents: List[Document] = [
        Document(page_content=chunk) for chunk in chunks
    ]

    # Fake embeddings (free, no API key)
    embeddings = FakeEmbeddings(size=128)

    # Create FAISS vector database
    VECTOR_DB = FAISS.from_documents(documents, embeddings)

    return {"message": "Document uploaded and processed successfully"}


# -------------------------------
# 💬 Ask Question API
# -------------------------------

@app.post("/ask")
def ask_question(question: str):
    global VECTOR_DB

    if VECTOR_DB is None:
        return {"error": "Please upload document first"}

    # Retrieve relevant documents
    docs = VECTOR_DB.similarity_search(question, k=3)

    context = "\n\n".join([doc.page_content for doc in docs])

    # Generate response using simple LLM
    answer = simple_llm(context, question)

    return {
        "question": question,
        "answer": answer
    }


# -------------------------------
# 🌐 Simple Frontend (Chat UI)
# -------------------------------

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>AI Customer Support Bot</title>

        <style>
            body {
                font-family: Arial;
                background: #343541;
                color: white;
                margin: 0;
            }

            #chat {
                height: 75vh;
                overflow-y: auto;
                padding: 20px;
            }

            .msg {
                margin: 10px;
                padding: 10px;
                border-radius: 8px;
                max-width: 60%;
            }

            .user {
                background: #10a37f;
                margin-left: auto;
            }

            .bot {
                background: #444654;
            }

            #input-area {
                position: fixed;
                bottom: 0;
                width: 100%;
                display: flex;
                padding: 10px;
                background: #40414f;
            }

            input {
                flex: 1;
                padding: 10px;
                border-radius: 5px;
                border: none;
            }

            button {
                margin-left: 10px;
                padding: 10px;
                border: none;
                background: #10a37f;
                color: white;
                cursor: pointer;
            }
        </style>
    </head>

    <body>

    <h2 style="text-align:center;">🤖 AI Customer Support Bot</h2>

    <div style="text-align:center;">
        <input type="file" id="file">
        <button onclick="upload()">Upload FAQ</button>
    </div>

    <div id="chat"></div>

    <div id="input-area">
        <input id="input" placeholder="Ask your question...">
        <button onclick="send()">Send</button>
    </div>

    <script>

    function addMsg(text, type){
        let div = document.createElement("div");
        div.className = "msg " + type;
        div.innerText = text;
        document.getElementById("chat").appendChild(div);
        div.scrollIntoView();
    }

    async function upload(){
        let file = document.getElementById("file").files[0];

        if(!file){
            alert("Please select a file");
            return;
        }

        let formData = new FormData();
        formData.append("file", file);

        let res = await fetch("/upload-doc", {
            method: "POST",
            body: formData
        });

        let data = await res.json();
        alert(data.message);
    }

    async function send(){
        let input = document.getElementById("input");
        let question = input.value;

        if(!question) return;

        addMsg(question, "user");

        let res = await fetch("/ask?question=" + encodeURIComponent(question), {
            method: "POST"
        });

        let data = await res.json();

        addMsg(data.answer || data.error, "bot");

        input.value = "";
    }

    </script>

    </body>
    </html>
    """