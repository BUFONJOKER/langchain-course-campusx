from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
from langchain_community.document_loaders import WebBaseLoader
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.header("Question Answering from any Blog or Web Page")

model = ChatOllama(model='gpt-oss:20b-cloud')

parser = StrOutputParser()

prompt = PromptTemplate(
    template = "Answer this question \n {question} from following text \n {text}"
)

url = st.text_input("Enter the URL of the blog or web page you want to ask questions about:")

question = st.text_input("Enter your question:")



if st.button("Get Answer"):
    
    loader = WebBaseLoader(url)

    text = loader.load()[0].page_content

    chain = prompt | model | parser

    input_data = {
        'question': question,
        'text': text
    }
    with st.spinner("Generating Response...", show_time=True):
        result = chain.invoke(input_data)

    st.markdown(f"## Answer:\n\n{result}")