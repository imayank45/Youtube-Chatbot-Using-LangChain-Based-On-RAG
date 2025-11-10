# 🎬 YouTube Chatbot — *RAG-based using LangChain*

> 🚀 A powerful **Retrieval-Augmented Generation (RAG)** chatbot that lets you ask questions about any YouTube video!  
> Built using **LangChain**, **OpenAI**, and **Streamlit** — with real-time transcript fetching and contextual Q&A.

---

## 🌟 Features

✅ **Automatic Transcript Fetching** — Extracts YouTube video transcripts using the YouTube Transcript API  
✅ **Text Chunking** — Splits transcripts into overlapping text chunks for better context retrieval  
✅ **Embeddings Generation** — Uses *OpenAI’s `text-embedding-3-small`* model  
✅ **FAISS Vector Store** — Efficient vector-based retrieval for semantic search  
✅ **RAG Pipeline** — Combines context + query for accurate and grounded answers  
✅ **Interactive Chat UI** — Clean Streamlit interface with sidebar loading animation  
✅ **Continuous Conversation** — The chatbot keeps asking questions interactively  

---

## 🧠 RAG (Retrieval-Augmented Generation) Workflow

Here’s how the system works step-by-step:

1. **🎥 Fetch Transcript:**  
   The YouTube transcript is fetched via `youtube_transcript_api`.

2. **✂️ Split Transcript:**  
   The transcript is divided into manageable chunks using LangChain’s `RecursiveCharacterTextSplitter`.

3. **🧩 Create Embeddings:**  
   Each chunk is converted into vector embeddings using `OpenAIEmbeddings`.

4. **🗄️ Store in FAISS:**  
   These embeddings are stored in a **FAISS** vector store for efficient similarity search.

5. **🔍 Retrieve Context:**  
   When the user asks a question, the top similar chunks (context) are retrieved.

6. **💬 Generate Answer:**  
   The **Main Chain** merges the question + retrieved context and passes it to an LLM to generate a context-aware answer.

---

## 🗂️ Project Structure

```bash
YOUTUBE-CHATBOT-USING-LANGCHAIN-BASED-ON-RAG/
│
├── notebooks/
│   └── RAG_Using_LangChain.ipynb          # Notebook for prototype & testing
│
├── src/
│   ├── chains/
│   │   ├── main_chain.py                  # Builds final RAG chain
│   │   ├── parallel_chain.py              # Combines retriever + user query
│   │   └── prompts/
│   │       └── qa_prompt.py               # Custom prompt template for QA
│   │
│   ├── utils/
│   │   ├── embeddings.py                  # Handles embedding creation
│   │   ├── retrieval.py                   # Retriever and FAISS setup
│   │   ├── text_splitter.py               # Transcript chunking logic
│   │   └── youtube_loader.py              # Fetches YouTube transcripts
│
├── app.py                                 # Streamlit main app
├── .env                                   # OpenAI API key
├── requirements.txt                       # Dependencies
├── LICENSE
└── README.md                              # Project documentation
