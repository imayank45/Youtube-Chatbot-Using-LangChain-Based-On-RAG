import streamlit as st
from src.utils.youtube_loader import fetch_youtube_transcript
from src.utils.text_splitter import divide_transcript_into_chunks
from src.utils.embeddings import store_embedidngs_in_vector_db
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()


st.title("🎥 YouTube Chatbot (RAG-based)")
st.markdown("Enter a YouTube video ID to fetch its transcript and start chatting.")


# Input field for YouTube ID
youtube_id = st.text_input("🔗 Enter YouTube Video URL:")
 
if youtube_id:
    with st.spinner("Fetching transcript..."):
        transcript_text = fetch_youtube_transcript(youtube_id)
    
    if transcript_text:
        st.success("✅ Transcript fetched successfully!")
        st.text_area("📜 Transcript Preview (first 2000 chars):", transcript_text[:2000], height=300)
        
 
        # text splitter
        chunks = divide_transcript_into_chunks(transcript_text)

        if chunks:
            st.success(f"✅ Transcript divided into {len(chunks)} chunks!")
            st.write("📄 Chunk Preview:")
            for i, chunk in enumerate(chunks[:3]):  # Display first 3 chunks
                st.text_area(f"Chunk {i+1}:", chunk.page_content, height=150)
                
        
        # generate embeddings and store in vector DB
        embeddings = OpenAIEmbeddings(
            model = "text-embedding-3-small"
        )
        
        vector_store = store_embedidngs_in_vector_db(chunks, embeddings)
        st.success("✅ Embeddings generated and stored in vector database!")
        st.write('Preview of vector store:')
        st.write(vector_store.index_to_docstore_id)
        st.write("You can now proceed to build a chatbot interface using this vector store.")