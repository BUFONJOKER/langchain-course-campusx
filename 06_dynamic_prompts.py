from langchain_core.prompts import PromptTemplate, load_prompt
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.header("Research Papers Assistant using dynamic prompts")

research_paper = st.selectbox(
    label="Select the research paper",
    options=[
        "Attention is all you need",
        "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding",
        "GPT-3: Language Models are Few-Shot Learners",
        "DALL-E: Creating Images from Text",
        "AlphaFold: Using AI for scientific discovery"
    ],
    key="research_paper"
)

paper_style = st.selectbox(
    label="Select the research paper style",
    options=['mathematical', 'code-oriented', 'visual', 'concise', 'detailed'],
    key="paper_style"
)

template = load_prompt("prompt_template.json")


model = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task='text-generation',
)

chat_model = ChatHuggingFace(llm=model)

prompt = template.invoke(
    {'research_paper':research_paper,
    'paper_style':paper_style}
)
if st.button("Summarize"):
    output = chat_model.invoke(prompt)
    
    st.write(output.content)
