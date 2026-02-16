from langchain_community.document_loaders import WebBaseLoader
import streamlit as st

url = "https://www.ibm.com/think/topics/ai-agents"

loader = WebBaseLoader(url)

document = loader.load()

st.header("Web Based Loader")

st.write(document[0].page_content)