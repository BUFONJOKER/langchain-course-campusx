from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
import streamlit as st

st.set_page_config(page_title='Runnables')

st.header("Runnables Sequence Joke Generator")

model = ChatOllama(model='gpt-oss:20b-cloud')

parser = StrOutputParser()

prompt = PromptTemplate(
    template="Generate joke on {topic}"
)

prompt2 = PromptTemplate(
    template = "Explain this joke \n {joke}"
)

topic = st.text_input("Write topic")

if st.button("Generate", type='primary'):

    chain = RunnableSequence(prompt, model, parser, prompt2, model, parser)

    result = chain.invoke({'topic':topic})
    
    st.write(result)