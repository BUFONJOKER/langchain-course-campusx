from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
import streamlit as st

st.header("Directory Loader Example")

loader = DirectoryLoader("../books", glob="**/*.pdf", loader_cls=PyPDFLoader)

documents = loader.lazy_load()

# st.write(f"Loaded {len(documents)} documents from the directory.")

# st.write(f"First document content:\n\n{documents[0].page_content}...")

for docs in documents:
    st.write(docs.metadata)