from langchain_ollama import ChatOllama
from langchain_community.document_loaders import PyPDFLoader
import streamlit as st

st.header("PDF Loader")

loader = PyPDFLoader("../file.pdf")

docs = loader.load()

text = st.text_input("Enter page Number to View")

if st.button("View", type='primary'):

    text = int(text)

    st.write(len(docs))

    st.write(docs[text].metadata)

    st.write(docs[text].page_content)
