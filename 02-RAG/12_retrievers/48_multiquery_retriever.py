from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain_classic.retrievers import MultiQueryRetriever
from langchain_core.documents import Document
import streamlit as st
load_dotenv()

st.title("MultiQuery Retriever")

docs  = [
    Document(page_content="Regular walking boosts heart health and can reduce symptoms of depression.", metadata={"source": "H1"}),
    Document(page_content="Consuming leafy greens and fruits helps detox the body and improve longevity.", metadata={"source": "H2"}),
    Document(page_content="Deep sleep is crucial for cellular repair and emotional regulation.", metadata={"source": "H3"}),
    Document(page_content="Mindfulness and controlled breathing lower cortisol and improve mental clarity.", metadata={"source": "H4"}),
    Document(page_content="Drinking sufficient water throughout the day helps maintain metabolism and energy.", metadata={"source": "H5"}),
    Document(page_content="The solar energy system in modern homes helps balance electricity demand.", metadata={"source": "I1"}),
    Document(page_content="Python balances readability with power, making it a popular system design language.", metadata={"source": "I2"}),
    Document(page_content="Photosynthesis enables plants to produce energy by converting sunlight.", metadata={"source": "I3"}),
    Document(page_content="The 2022 FIFA World Cup was held in Qatar and drew global energy and excitement.", metadata={"source": "I4"}),
    Document(page_content="Black holes bend spacetime and store immense gravitational energy.", metadata={"source": "I5"}),
]

embeddings = HuggingFaceEndpointEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")

vectorstore = FAISS.from_documents(docs, embeddings)

model = ChatOllama(model='gpt-oss:120b-cloud', verbose=True)

similarity_retriever = vectorstore.as_retriever(
    search_type='similarity', search_kwargs={'k': 3}
)

multiquery_retriever = MultiQueryRetriever.from_llm(
    retriever=vectorstore.as_retriever(search_kwargs={'k': 3}), llm=model
)

query = "How to improve energy levels and maintain balance?"

similarity_results = similarity_retriever.invoke(query)
multiquery_results = multiquery_retriever.invoke(query)

st.subheader("Similarity Retriever Results")
for i, doc in enumerate(similarity_results):
    st.write(f"Document {i+1} (Source: {doc.metadata['source']}):")
    st.write(doc.page_content)
    st.write("\n---\n")

st.subheader("MultiQuery Retriever Results")
for i, doc in enumerate(multiquery_results):
    st.write(f"Document {i+1} (Source: {doc.metadata['source']}):")
    st.write(doc.page_content)
    st.write("\n---\n")