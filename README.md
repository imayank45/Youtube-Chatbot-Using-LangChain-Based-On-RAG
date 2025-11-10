🎥 YouTube Chatbot (RAG-based)

A Retrieval-Augmented Generation (RAG)-based chatbot built using LangChain, Streamlit, and OpenAI.
This chatbot allows users to input a YouTube video URL, automatically fetches its transcript, stores it in a vector database, and enables users to ask questions related to the video.

🚀 Features

✅ Fetch YouTube video transcripts automatically
✅ Split large transcripts into meaningful chunks
✅ Generate embeddings using OpenAI Embedding Model
✅ Store and retrieve embeddings using FAISS vector store
✅ Context-aware question-answering powered by LangChain RAG pipeline
✅ Interactive Streamlit UI with sidebar loading animations
✅ Repeated chatbot conversation interface

🧠 RAG (Retrieval-Augmented Generation) Workflow

Fetch Transcript: Extracts transcript text from the YouTube video using youtube_transcript_api.

Text Splitting: Breaks down the transcript into smaller overlapping chunks using LangChain’s RecursiveCharacterTextSplitter.

Embedding Generation: Converts each chunk into vector embeddings using OpenAI’s text-embedding-3-small.

Vector Store: Stores these embeddings in a FAISS vector database for efficient retrieval.

Retriever: Fetches top relevant chunks (context) based on user queries.

Main Chain: Combines user queries and retrieved context → passes it through a language model → generates answers.

Streamlit UI: Provides an easy-to-use web interface for end-to-end interaction.

🏗️ Project Structure
YOUTUBE-CHATBOT-USING-LANGCHAIN-BASED-ON-RAG/
│
├── notebooks/
│   └── RAG_Using_LangChain.ipynb         # Notebook for experimentation
│
├── src/
│   ├── chains/
│   │   ├── main_chain.py                 # Main RAG chain combining retriever and LLM
│   │   ├── parallel_chain.py             # RunnableParallel chain for context + question
│   │   └── prompts/
│   │       └── qa_prompt.py              # Custom QA prompt template
│   │
│   ├── utils/
│   │   ├── embeddings.py                 # Handles embedding generation & storage
│   │   ├── retrieval.py                  # Retriever and vector store setup
│   │   ├── text_splitter.py              # Splits transcript into smaller chunks
│   │   └── youtube_loader.py             # Fetches YouTube transcripts
│
├── youtube-chatbot/                      # (Optional) Data or model folder
│
├── app.py                                # Streamlit app (main entry point)
├── .env                                  # Environment variables (API keys)
├── .gitignore
├── LICENSE
├── requirements.txt                      # Python dependencies
└── README.md                             # You’re reading it!

🖼️ Screenshot

You can add your project screenshots in the repository and display them here:

![App Screenshot](./assets/screenshot.png)


👉 Place your screenshot (e.g., Screenshot 2025-11-11 at 2.09.34 AM.png) in a folder named assets/ inside your root directory:

assets/
 └── screenshot.png

⚙️ Installation & Setup

Clone the repository

git clone https://github.com/yourusername/Youtube-Chatbot-RAG.git
cd Youtube-Chatbot-RAG


Create a virtual environment

python3 -m venv youtube-chatbot
source youtube-chatbot/bin/activate   # (Mac/Linux)
youtube-chatbot\Scripts\activate      # (Windows)


Install dependencies

pip install -r requirements.txt


Set up environment variables

Create a .env file in the project root and add:

OPENAI_API_KEY=your_openai_api_key


Run the app

streamlit run app.py


Open in browser

http://localhost:8501

💬 How It Works in Streamlit

Enter a YouTube video URL

The app fetches its transcript

Splits transcript → Generates embeddings → Stores in FAISS

Ask your questions in the chat interface

The chatbot retrieves relevant parts of the video and answers intelligently

🧩 Tech Stack
Component	Library/Tool
Frontend	Streamlit
LLM	OpenAI GPT Models
Embeddings	OpenAI Embeddings
Vector DB	FAISS
Orchestration	LangChain
Transcript Fetch	youtube_transcript_api
📄 License

This project is licensed under the MIT License — feel free to use and modify it.
