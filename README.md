# 🤖 AI Customer Support Bot

An AI-powered customer support chatbot built using **FastAPI** and **LangChain**, designed to answer user queries based on uploaded documents (like FAQs, product descriptions, etc.).

---

## 🚀 Features

* 📄 Upload any text document (FAQ, product info, etc.)
* 🧠 Automatically process and split content into chunks
* 🔍 Semantic search using vector database
* 💬 Ask questions and get AI-generated answers
* 🌐 Clean ChatGPT-like web interface
* ⚡ FastAPI backend (high performance)
* 🆓 Fully FREE setup (no paid APIs required)

---

## 🧠 How It Works

1. **Upload Document**

   * User uploads a `.txt` file (FAQ, product details, etc.)

2. **Text Processing**

   * Text is split into smaller chunks using a text splitter

3. **Embedding Creation**

   * Fake embeddings are generated (for demo purposes)

4. **Vector Storage**

   * Data is stored in FAISS vector database

5. **User Query**

   * User asks a question

6. **Retrieval + Answer**

   * Relevant chunks are retrieved
   * LLM generates answer based on context

---

## 🛠️ Tech Stack

* **Backend:** FastAPI
* **AI Framework:** LangChain
* **Vector Database:** FAISS
* **Frontend:** HTML, CSS, JavaScript
* **Embeddings:** FakeEmbeddings (free)
* **LLM:** Custom Simple LLM (no API cost)

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-customer-support-bot.git
cd ai-customer-support-bot
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install fastapi uvicorn python-multipart
pip install langchain langchain-community langchain-core
pip install faiss-cpu
```

---

### ⚠️ Important Note

* Use **Python 3.10 or 3.11**
* Avoid Python 3.14 (compatibility issues with LangChain & FAISS)

---

## ▶️ Run the Application

```bash
uvicorn app.main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000
```

---

## 📂 API Endpoints

### 1. Upload Document

```
POST /upload-doc
```

* Upload `.txt` file
* Stores processed data in vector DB

---

### 2. Ask Question

```
POST /ask?question=your_question
```

* Returns AI-generated answer based on uploaded document

---

### 3. Web UI

```
GET /
```

* Chat interface (like ChatGPT)

---

## 📸 UI Preview

* Upload file button
* Chat interface
* Real-time question-answer system

---

## ⚙️ Project Structure

```
ai-customer-support-bot/
│
├── app/
│   └── main.py
│
├── venv/
├── README.md
└── requirements.txt
```

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

---

## 📄 License

This project is open-source and free to use.

---

## 🙌 Author

Built by Deepanshu
Aspiring AI Developer 🚀

---

## ⭐ Support

If you like this project:

* ⭐ Star the repo
* 🔗 Share with others
* 💬 Give feedback

---
