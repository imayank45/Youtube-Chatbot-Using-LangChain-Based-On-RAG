import streamlit as st
from src.utils.youtube_loader import fetch_youtube_transcript
from src.utils.text_splitter import divide_transcript_into_chunks
from src.utils.embeddings import store_embedidngs_in_vector_db
from src.utils.retrieval import get_context_embeddings
from src.chains.main_chain import build_main_chain
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

# ------------------------ 🎨 PAGE CONFIG ------------------------
st.set_page_config(page_title="🎥 YouTube RAG Chatbot", layout="wide")
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    textarea, input {
        background-color: #1e1e1e !important;
        color: #ffffff !important;
    }
    .stTextInput>div>div>input {
        border-radius: 10px;
    }
    .stChatMessage {
        padding: 0.8rem;
        border-radius: 1rem;
        margin-bottom: 0.5rem;
    }
    .user-msg {
        background-color: #2e8b57;
    }
    .bot-msg {
        background-color: #1e3a8a;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------------ ⚙️ MAIN UI ------------------------
st.title("🎬 YouTube Chatbot (RAG-based)")
st.markdown("Fetch a transcript, create embeddings, and chat with your video 💬")

# Sidebar Loading Steps
st.sidebar.header("📊 Processing Steps")
progress = st.sidebar.empty()

# Input field for YouTube ID
youtube_id = st.text_input("🔗 Enter YouTube Video URL:")

if youtube_id:
    progress.info("Fetching transcript...")
    with st.spinner("Fetching transcript..."):
        transcript_text = fetch_youtube_transcript(youtube_id)
    progress.success("✅ Transcript fetched!")

    if transcript_text:
        st.success("✅ Transcript fetched successfully!")
        st.text_area("📜 Transcript Preview (first 2000 chars):", transcript_text[:2000], height=300)

        progress.info("Splitting transcript into chunks...")
        chunks = divide_transcript_into_chunks(transcript_text)
        if chunks:
            progress.success("✅ Transcript divided successfully!")

            st.success(f"✅ Transcript divided into {len(chunks)} chunks!")
            for i, chunk in enumerate(chunks[:3]):  # Display first 3 chunks
                st.text_area(f"Chunk {i+1}:", chunk.page_content, height=150)

            progress.info("Generating embeddings...")
            embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
            vector_store = store_embedidngs_in_vector_db(chunks, embeddings)
            if vector_store:
                progress.success("✅ Embeddings generated!")
                st.success("✅ Embeddings generated and stored in vector database!")

                retriever = get_context_embeddings(vector_store)
                st.success("✅ Retriever created successfully!")

                main_chain = build_main_chain(retriever)
                
                # small helper to safely invoke RAG chain
                def ask_with_context(chain, retriever, user_query):
                    # get retrieved context
                    retrieved_docs = retriever.get_relevant_documents(user_query)
                    if not retrieved_docs:
                        return "Sorry, I couldn't find any relevant part of the video."

                    # combine docs as context
                    context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)

                    # invoke chain correctly
                    try:
                        response = chain.invoke({
                            "context": context_text,
                            "question": user_query
                        })
                    except Exception as e:
                        response = f"Error while generating answer: {str(e)}"
                    return response


                # ------------------------ 💬 CHAT SECTION ------------------------
                st.markdown("### 💭 Ask Questions about the Video")

                if "chat_history" not in st.session_state:
                    st.session_state.chat_history = []

                user_question = st.chat_input("Ask a question about the video...")

                if user_question:
                    st.session_state.chat_history.append({"role": "user", "content": user_question})

                    with st.spinner("Generating answer..."):
                        answer = main_chain.invoke(user_question)


                    st.session_state.chat_history.append({"role": "assistant", "content": answer})

                # Display chat history
                for chat in st.session_state.chat_history:
                    if chat["role"] == "user":
                        st.chat_message("user").markdown(f"**You:** {chat['content']}")
                    else:
                        st.chat_message("assistant").markdown(f"**Bot:** {chat['content']}")
