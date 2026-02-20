from prompt_context_54 import prompt, context_from_docs
from langchain_core.runnables import RunnableParallel, RunnableLambda, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from model_55 import model

parser = StrOutputParser()


def build_chain(retriever):

    parallel_chain = RunnableParallel(
        {
            "context": retriever | RunnableLambda(context_from_docs),
            "question": RunnablePassthrough(),
        }
    )
    return parallel_chain | prompt | model | parser


def answer_question(question: str, retriever):

    chain = build_chain(retriever)
    
    return chain.invoke(question)