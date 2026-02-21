from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import (
    RunnableSequence, RunnableParallel, RunnablePassthrough
)
import streamlit as st

st.set_page_config(page_title='Runnables')

st.header("Runnables Passthrough Joke Generator")

model = ChatOllama(model='gpt-oss:20b-cloud')

parser = StrOutputParser()

prompt = PromptTemplate(
    template="Generate joke on {topic}"
)

prompt2 = PromptTemplate(
    template = "Explain this joke \n {joke}"
)

topic = st.text_input("Write topic")

if st.button("Generate", icon=":material/auto_awesome:", type='primary'):

    joke_gen_chain = RunnableSequence(prompt, model, parser)
    
    explain_gen_chain = RunnableParallel({
        'joke': RunnablePassthrough(),
        'explain':RunnableSequence(prompt2, model, parser)
    })

    chain = RunnableSequence(joke_gen_chain, explain_gen_chain)

    result = chain.invoke({'topic':topic})
    
    st.markdown("## Joke")
    
    st.write(result['joke'])
    
    st.markdown("## Explaination")

    st.write(result['explain'])