from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv
import streamlit as st

st.title("Maximal Marginal Relevance (MMR) Retriever")

load_dotenv()

embeddings = HuggingFaceEndpointEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")

docs = [
    Document(page_content="LangChain makes it easy to work with LLMs."),
    Document(page_content="LangChain is used to build LLM based applications."),
    Document(page_content="Chroma is used to store and search document embeddings."),
    Document(page_content="Embeddings are vector representations of text."),
    Document(page_content="MMR helps you get diverse results when doing similarity search."),
    Document(page_content="LangChain supports Chroma, FAISS, Pinecone, and more."),
]

vectorstore = FAISS.from_documents(docs, embeddings)

retriever = vectorstore.as_retriever(
    search_type="mmr", search_kwargs={"k": 3, "lambda_mult": 0}
)

results = retriever.invoke("What is LangChain?")

st.subheader("MMR Results:")

for i, doc in enumerate(results):
    st.write(f"Document {i+1}:")
    st.write(doc.page_content)
    st.write("\n---\n")

