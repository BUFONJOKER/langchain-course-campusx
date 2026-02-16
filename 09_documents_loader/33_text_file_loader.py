from langchain_community.document_loaders import TextLoader
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
import streamlit as st

st.header("Text File Loader")

model = ChatOllama(model='gpt-oss:20b-cloud')

loader = TextLoader("../file.txt", encoding="utf-8")

documents = loader.load()

prompt = PromptTemplate(
    template = 'Generate title of this text \n {text}'
)

parser = StrOutputParser()

chain = prompt | model | parser

text = documents[0].page_content

result = chain.invoke(text)

st.markdown(f"### {result}")

st.write(documents[0].page_content)  # Full text content
# st.write(documents[0].metadata)      # {'source': 'path/to/file.txt'}