from langchain_core.runnables import RunnableParallel
from langchain_ollama import ChatOllama
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import streamlit as st
import time

load_dotenv()

st.set_page_config(page_title="Notes and Quiz")

st.header("Notes and Quiz Generator")

text = st.text_input("Write text")

parser = StrOutputParser()

model_1 = ChatOllama(model='gpt-oss:20b-cloud')

model_2 = HuggingFaceEndpoint(
        repo_id='Qwen/Qwen2-7B-instruct',
        task='text-generation',
)

model_2 = ChatHuggingFace(llm=model_2)



if st.button("Generate", type='primary'):
    
    start = time.time()

    template_1 = PromptTemplate.from_template(
        template='Generate short and simple notes from following text \n {text}'
    )

    template_2 = PromptTemplate.from_template(
        template='Generate 5 questions answer from following text \n {text}'
    )

    template_3 = PromptTemplate.from_template(
        template='Merge the provided notes and quiz into single document \n notes -> {notes} and \n quiz -> {quiz}'
    )

    parallel_chains = RunnableParallel(
        {
            'notes': template_1 | model_1 | parser,
            'quiz' : template_2 | model_2 | parser
        }
    )

    merge_chains = template_3 | model_1 | parser

    chain = parallel_chains | merge_chains

    result = chain.invoke({'text':text})

    end = time.time()

    st.write(f"Response generated in {(end-start):.2f} seconds")

    st.write(result)

