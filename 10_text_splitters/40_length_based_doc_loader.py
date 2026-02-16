from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
import streamlit as st

loader = PyPDFLoader("../books/ch5.pdf")

docs = loader.load()

st.title("Character Text Splitter with Documents Loader Example")

    
# Create a CharacterTextSplitter with a chunk size of 20 characters
text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=10, separator="")

# Split the text into chunks
chunks = text_splitter.split_documents(docs)

st.write("len(chunks):", len(chunks))

st.write("Chunks:")

for i, chunk in enumerate(chunks):

    st.write(f"Chunk {i+1} page content: {chunk.page_content}")