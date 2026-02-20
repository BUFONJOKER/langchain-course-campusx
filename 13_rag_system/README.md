# 🎥🤖 YouTube Chatbot with RAG System

An intelligent **YouTube Question-Answering Chatbot** built using **Retrieval-Augmented Generation (RAG)**.
This system extracts video transcripts, stores embeddings in a vector database, and generates accurate answers using an LLM.

---

## 📌 Project Workflow

---

## 🔗 1️⃣ Get YouTube Video URL

* Accept a YouTube video link as input
* Extract the video ID
* Prepare it for transcript processing

---

## 📝 2️⃣ Extract Video Transcript

* Fetch transcript using:

  * `youtube-transcript-api`
  * YouTube Loader (LangChain)
* Convert transcript into a **LangChain Document**

✔️ Structured format
✔️ Ready for chunking

---

## ✂️ 3️⃣ Split Transcript into Chunks

* Use **Recursive Character Text Splitter**
* Break large transcript into smaller overlapping chunks

📦 Why?

* Improves retrieval accuracy
* Maintains context
* Handles long videos efficiently

---

## 🧠 4️⃣ Create Embeddings & Store in Vector Database

* Generate embeddings using a **Hugging Face Embedding Model**
* Store embeddings inside **FAISS Vector Store**

### 🗄️ Tech Used:

* 🧮 Embedding Model → Hugging Face
* 📚 Vector Database → FAISS

This enables **semantic search** over the transcript.

---

## 🔍 5️⃣ Create Retriever

* Convert FAISS vector store into a **Retriever**
* Retrieve top relevant chunks based on user query

🎯 Ensures:

* Context-aware retrieval
* Reduced hallucination
* More accurate answers

---

## 🧾 6️⃣ Create Prompt

* Combine:

  * Retrieved relevant chunks
  * User question

📄 Structured prompt ensures the LLM:

* Uses only relevant context
* Generates grounded responses

---

## 🤖 7️⃣ Generate Final Answer

* Use **Ollama model:** `gpt-oss:120b-cloud`
* Generate response using RAG pipeline

🚀 Produces:

* Context-aware answers
* Accurate video-based responses
* Reduced hallucinations

---

# 🏗️ Architecture Overview

```text
YouTube URL
     ↓
Transcript Extraction
     ↓
Document Chunking
     ↓
Embeddings (Hugging Face)
     ↓
FAISS Vector Store
     ↓
Retriever
     ↓
Prompt Construction
     ↓
LLM (Ollama gpt-oss:120b-cloud)
     ↓
Final Answer
```

---

# ✨ Key Features

* 📺 Ask questions about any YouTube video
* 🧠 Semantic search with embeddings
* 📚 FAISS-based vector storage
* 🔍 Intelligent retrieval
* 🤖 Large-scale LLM answer generation
* ⚡ RAG-based architecture for higher accuracy

---

