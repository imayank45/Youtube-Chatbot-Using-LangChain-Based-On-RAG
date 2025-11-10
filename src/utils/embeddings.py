from langchain_community.vectorstores import FAISS

def store_embedidngs_in_vector_db(chunks, embeddings):
    
    vector_store = FAISS.from_documents(chunks, embeddings)
    return vector_store