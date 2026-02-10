from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task='text-generation'
)

chat_model = ChatHuggingFace(llm=model)

st.header("Summarizer")

user_input = st.text_input(label="Enter Prompt")

if st.button(label="Summarize"):

    output = chat_model.invoke(user_input)
    
    st.write(output.content)