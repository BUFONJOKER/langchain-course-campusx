from langchain_text_splitters import RecursiveCharacterTextSplitter
import streamlit as st

st.title("Text Structure Based Text Splitter")

text = """LangChain is a framework for developing applications powered by language models. It provides a standard interface for all components and a toolkit for connecting them together. The core idea is that we can "chain" together different components to create more advanced use cases around LLMs. For example, we can chain together a LLM with a prompt template and a few other components to create a question-answering bot. The framework also provides end-to-end chains, which are chains that take in an input and produce an output, without the user having to worry about the intermediate steps."""

st.subheader("Original Text")

st.write(text)

text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=0)

chunks = text_splitter.split_text(text)

st.subheader("Chunks Length")

st.write(len(chunks))

for i, chunk in enumerate(chunks):
    st.subheader(f"Chunk {i+1}")
    st.write(chunk)

