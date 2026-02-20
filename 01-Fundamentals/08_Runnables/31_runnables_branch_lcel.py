from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import (
    RunnablePassthrough, RunnableLambda, RunnableBranch
)
import streamlit as st

st.set_page_config(page_title='Runnables')

st.header("Runnables Branch topic Explanation and Summarize if words > 500")

model = ChatOllama(model='gpt-oss:20b-cloud')

parser = StrOutputParser()

prompt = PromptTemplate(
    template="Generate explanation on {topic}"
)

prompt2 = PromptTemplate(
    template="Summarize the following text \n {text}"
)

topic = st.text_input("Write topic")

if st.button("Generate", icon=":material/auto_awesome:", type='primary'):

    explain_gen_chain = prompt | model | parser
    
    branch_chain = RunnableBranch(
        (lambda x: len(x.split())>500, prompt2 | model | parser),
        RunnablePassthrough()
    )

    chain = explain_gen_chain | branch_chain

    result = chain.invoke({'topic':topic})
    
    st.markdown("## Explanation")
    
    st.write(result)
    
    