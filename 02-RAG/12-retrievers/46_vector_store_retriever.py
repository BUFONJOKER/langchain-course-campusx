from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from langchain_core.documents import Document
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

embeddings = HuggingFaceEndpointEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")

documents = [
    Document(page_content="LangChain helps developers build LLM applications easily."),
    Document(page_content="Chroma is a vector database optimized for LLM-based search."),
    Document(page_content="Embeddings convert text into high-dimensional vectors."),
    Document(page_content="OpenAI provides powerful embedding models."),
]

vector_store = Chroma.from_documents(documents, embeddings, collection_name="my_collection")

retriever = vector_store.as_retriever(search_kwargs={"k":2})

query = "What is LangChain?"

retrieved_docs = retriever.invoke(query)

for i, doc in enumerate(retrieved_docs):
    st.write(f"Retrieved Document {i+1}:")
    st.write(doc.page_content)
    st.write("\n---\n")

similarity_scores = vector_store.similarity_search_with_relevance_scores(query, k=2)

for i, (doc, score) in enumerate(similarity_scores):
    st.write(f"Document {i+1} (Score: {score:.4f})")
    st.write(doc.page_content)
    st.write("\n---\n")