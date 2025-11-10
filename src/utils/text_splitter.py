from langchain.text_splitter import RecursiveCharacterTextSplitter

# divide transcript into chunks
def divide_transcript_into_chunks(transcript: str):
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    
    chunks = text_splitter.create_documents(
        [transcript]
    )

    return chunks