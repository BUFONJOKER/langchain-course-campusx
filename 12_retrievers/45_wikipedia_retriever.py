from langchain_community.retrievers import WikipediaRetriever
import streamlit as st

st.title("Wikipedia Retriever")

retriever = WikipediaRetriever()

query = "the geopolitical history of india and pakistan from the perspective of a chinese"

docs = retriever.invoke(query)

# st.write(docs[0].page_content)

st.write(len(docs))

for i, doc in enumerate(docs):
    st.write(f"Document {i+1}:")
    st.write(doc.page_content)
    st.write("\n---\n")