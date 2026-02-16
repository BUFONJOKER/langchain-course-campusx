from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import (
    RunnableSequence, RunnableParallel, RunnablePassthrough,
    RunnableLambda
)
import streamlit as st

st.set_page_config(page_title='Runnables')

st.header("Runnables Lambda Joke Generator and Words Counter")

model = ChatOllama(model='gpt-oss:20b-cloud')

parser = StrOutputParser()

prompt = PromptTemplate(
    template="Generate joke on {topic}"
)

topic = st.text_input("Write topic")

if st.button("Generate", icon=":material/auto_awesome:", type='primary'):

    joke_gen_chain = RunnableSequence(prompt, model, parser)
    
    words_count_chain = RunnableParallel({
        'joke': RunnablePassthrough(),
        'words':RunnableLambda(lambda text:len(text.split()))
    })

    chain = RunnableSequence(joke_gen_chain, words_count_chain)

    result = chain.invoke({'topic':topic})
    
    st.markdown("## Joke")
    
    st.write(result['joke'])
    
    st.markdown("## Words Count")

    st.write(result['words'])