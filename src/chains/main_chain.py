from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_openai import ChatOpenAI


def build_main_chain(retriever):
    """
    Builds the main RAG chain which:
    1️⃣ Retrieves relevant context based on user query
    2️⃣ Passes both context + question to the LLM
    3️⃣ Parses the response into clean text
    """

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)
    parser = StrOutputParser()

    # Format the retrieved documents into a single string
    def format_docs(docs):
        if not docs:
            return "No relevant information found in the transcript."
        return "\n\n".join(doc.page_content for doc in docs)

    # RunnableParallel handles context + question together
    parallel = RunnableParallel({
        # retriever only expects the plain question string
        "context": RunnableLambda(lambda x: retriever.get_relevant_documents(x)) | RunnableLambda(format_docs),
        "question": RunnablePassthrough()
    })

    # prompt template
    prompt = PromptTemplate(
        template="""
You are a helpful assistant. Use only the context from the video transcript to answer the question.
If the context is not sufficient, just say "I don't know."

Context:
{context}

Question:
{question}

Answer:""",
        input_variables=["context", "question"]
    )

    # Full pipeline
    main_chain = parallel | prompt | llm | parser
    return main_chain
