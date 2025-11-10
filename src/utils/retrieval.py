
def get_context_embeddings(vector_store):
    
    # retrieve top 4 documents form vector store
    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k":4}
    )
    
    return retriever