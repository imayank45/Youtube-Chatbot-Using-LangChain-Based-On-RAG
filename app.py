import streamlit as st
from src.utils.youtube_loader import fetch_youtube_transcript


st.title("🎥 YouTube Chatbot (RAG-based)")
st.markdown("Enter a YouTube video ID to fetch its transcript and start chatting.")


# Input field for YouTube ID
youtube_id = st.text_input("🔗 Enter YouTube Video URL:")
 
if youtube_id:
    with st.spinner("Fetching transcript..."):
        transcript_text = fetch_youtube_transcript(youtube_id)
    
    if transcript_text:
        st.success("✅ Transcript fetched successfully!")
        st.text_area("📜 Transcript Preview (first 2000 chars):", transcript_text, height=300)