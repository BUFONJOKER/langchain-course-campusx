from langchain_core.runnables import RunnableParallel
from langchain_ollama import ChatOllama
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.output_parsers import (
    StrOutputParser, PydanticOutputParser
)
from langchain_core.prompts import PromptTemplate

from langchain_core.runnables import RunnableBranch, RunnableLambda
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Literal
import streamlit as st
import time

load_dotenv()

st.set_page_config(page_title="Sentimentaor")

st.header("Sentiment of Given review (Positive or Negative)")

review = st.text_input("Write review")

parser = StrOutputParser()

model = ChatOllama(model='gpt-oss:20b-cloud')

class Review(BaseModel):

    sentiment : Literal['positive', 'negative'] = Field(description="Generate sentiment of review")

parser_pydantic = PydanticOutputParser(pydantic_object=Review)

parser_str = StrOutputParser()

prompt = PromptTemplate.from_template(
    template="""
    You are an expert linguistic analyst. Your task is to perform a detailed sentiment analysis 
    on the movie review provided below. 
    
    Review Content:
    {review}
    
    Instructions:
    Analyze the emotional tone, polarity, and key sentiments. 
    {format}
    """,
    partial_variables={'format': parser_pydantic.get_format_instructions()}
)

prompt_2 = PromptTemplate.from_template(
    template="""
    You are the Social Media Manager for a major film studio. 
    A fan has left a glowing 5-star review for our latest movie.
    
    Review: 
    "{review}"
    
    Task:
    Write a warm, enthusiastic, and professional response. 
    - Express genuine gratitude.
    - Match the fan's excitement.
    - Keep it under 3 sentences.
    """
)

prompt_3 = PromptTemplate.from_template(
    template="""
    You are a high-level Customer Relations Representative for a cinema chain. 
    A viewer had a poor experience and left a negative review.
    
    Review: 
    "{review}"
    
    Task:
    Write a professional and empathetic response. 
    - Acknowledge their specific frustrations.
    - Maintain a calm, helpful tone (never defensive).
    - Express a desire to improve and thank them for the feedback.
    - Keep it under 3 sentences.
    """
)

if st.button("Generate", type='primary'):
    
    st.markdown(f"### Using {model}")

    classifier_chain = prompt | model | parser_pydantic
    
    result = classifier_chain.invoke({'review':review})

    st.header("Sentiment")

    st.write(result.sentiment)

    branch_chain = RunnableBranch(
        (lambda x:x.sentiment=='positive', prompt_2 | model | parser_str),
        (lambda x:x.sentiment=='negative', prompt_3 | model | parser_str),
        RunnableLambda(lambda x: 'could not find sentiment')
    )

    chain = classifier_chain | branch_chain

    result = chain.invoke({'review':review})

    st.write(result)

    

    

    