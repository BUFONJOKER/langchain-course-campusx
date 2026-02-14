from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import time
import streamlit as st

st.set_page_config(page_title="Summarizer")

st.header("Summarizer")

topic = st.text_input(label="Write topic")

if st.button(label="Generate", type="primary"):
    
    template_1 = PromptTemplate.from_template(
    template='Generate detail report on {topic}'
    )

    template_2 = PromptTemplate.from_template(
        template='Genrate 5 pointer summary of following text \n {text}'
    )

    parser = StrOutputParser()

    model = ChatOllama(model='gpt-oss:20b-cloud')

    chain = template_1 | model | parser | template_2 | model | parser


    start = time.time()

    result = chain.invoke({'topic':topic})

    end = time.time()

    st.write(f"Response generated in : {(end-start):.2f}seconds")

    st.write(result)
