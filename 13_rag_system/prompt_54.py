from retriever_53 import retriever
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

question = "is the topic of aliens discussed in the video? if yes then what was discussed about it?"

retrieved_docs = retriever.invoke(question)

context = "\n\n".join(doc.page_content for doc in retrieved_docs)

final_prompt = prompt.invoke({'context': context, 'question': question})