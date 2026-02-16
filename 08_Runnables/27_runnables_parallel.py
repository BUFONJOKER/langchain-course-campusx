from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnableSequence
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.set_page_config(page_title="Tweet and Linkedin Post")
st.header("Runnables Parallel")
st.markdown("## Tweet Generator using Llama-3.1-8B-Instruct and Linkedin Post Generator using gpt-oss:20b-cloud")

model = HuggingFaceEndpoint(
    repo_id='meta-llama/Llama-3.1-8B-Instruct', task='text-generation'
)

model_tweet = ChatHuggingFace(llm=model)

model_linkedin = ChatOllama(model='gpt-oss:20b-cloud')

parser = StrOutputParser()

prompt_tweet = PromptTemplate(
    template='Generate Tweet on this topic \n {topic}'
)

prompt_linkedin = PromptTemplate(
    template = 'Generate LinkedIn Post on this topic \n {topic}'
)

topic = st.text_input("Write topic")

if st.button("Generate", icon=":material/auto_awesome:", type='primary'):

    chain = RunnableParallel({
        'tweet': RunnableSequence(prompt_tweet, model_tweet, parser),
        'linkedin': RunnableSequence(prompt_linkedin, model_linkedin, parser)
    })

    result = chain.invoke({'topic':topic})

    st.header("Tweet")

    st.write(result['tweet'])

    st.header('LinkedIn Post')

    st.write(result['linkedin'])