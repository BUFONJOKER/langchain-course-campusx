from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_core.documents import Document
import streamlit as st

load_dotenv()

st.title("Chroma Vector Store Example")

embeddings = HuggingFaceEndpointEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")

doc1 = Document(page_content="Shahid Afridi is a former Pakistani cricketer and captain of the Pakistan national cricket team. He is a all-rounder.", metadata={"team":"Peshawar Zalmi"})

doc2 = Document(page_content="Shoaib Akhtar is a former Pakistani cricketer and captain of the Pakistan national cricket team. He is a fast bowler.", metadata={"team":"Karachi Kings"})

doc3 = Document(page_content="Shoaib Malik is a former Pakistani cricketer and captain of the Pakistan national cricket team. He is a all-rounder.", metadata={"team":"Multan Sultans"})

doc4 = Document(page_content="Sarfraz Ahmed is a former Pakistani cricketer and captain of the Pakistan national cricket team. He is a wicket-keeper batsman.", metadata={"team":"Quetta Gladiators"})

doc5 = Document(page_content="Babar Azam is a Pakistani cricketer and captain of the Pakistan national cricket team. He is a batsman.", metadata={"team":"Karachi Kings"})

docs = [doc1, doc2, doc3, doc4, doc5]

vector_store = Chroma(
    collection_name="cricket_players",
    embedding_function=embeddings
)

vector_store.add_documents(docs)

data = vector_store.get()

st.write(data)

# st.write(vector_store.similarity_search("Who is the all-rounder from Peshawer Zalmi?", k=1))

# st.write(vector_store.similarity_search_with_score(
#     query="",
#     filter={"team": "Peshawar Zalmi"},
# ))