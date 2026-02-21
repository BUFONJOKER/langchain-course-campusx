from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template(
    '''
    You are a helpful assistant that provides information about the video based on the retrieved documents.
    Use the following context to answer the question.
    {context}
    if you don't know the answer, say you don't know.
    Question: {question}
    '''
)


def context_from_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)
