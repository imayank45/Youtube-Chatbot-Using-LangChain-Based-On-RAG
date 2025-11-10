from langchain_core.runnables import RunnableLambda, RunnableParallel, RunnablePassthrough

def format_docs(retrieved_docs):
    """Combine retrieved documents into a single context string."""
    return "\n\n".join(doc.page_content for doc in retrieved_docs)

def build_parallel_chain(retriever):
    """
    Properly connect retriever with the user question for RAG.
    - The retriever now takes the question as input.
    - The output will be a dict: {"context": <retrieved text>, "question": <original question>}
    """
    # Step 1: Given a question, retrieve top docs
    get_context = RunnableLambda(lambda x: retriever.invoke(x["question"])) | RunnableLambda(format_docs)

    # Step 2: Combine both question and context in parallel
    parallel = RunnableParallel({
        "context": get_context,
        "question": RunnableLambda(lambda x: x["question"])
    })

    return parallel
