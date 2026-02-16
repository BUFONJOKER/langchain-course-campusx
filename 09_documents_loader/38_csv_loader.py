from langchain_community.document_loaders import CSVLoader
import streamlit as st

loader = CSVLoader(file_path="../drug200.csv")

docs = loader.load()

st.write(len(docs))

st.header("CSV File Loader")

data = docs[1].metadata

st.write(data)