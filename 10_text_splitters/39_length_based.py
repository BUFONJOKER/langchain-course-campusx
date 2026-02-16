from langchain_text_splitters import CharacterTextSplitter
import streamlit as st

st.title("Character Text Splitter Example")

text = st.text_input("Enter some text to split:")

if st.button("Split Text", type="primary"):
    
    # Create a CharacterTextSplitter with a chunk size of 20 characters
    text_splitter = CharacterTextSplitter(chunk_size=20, chunk_overlap=0, separator="")

    # Split the text into chunks
    chunks = text_splitter.split_text(text)

    st.write("len(chunks):", len(chunks))

    st.write("Chunks:")

    for i, chunk in enumerate(chunks):

        st.write(f"Chunk {i+1}: {chunk}")