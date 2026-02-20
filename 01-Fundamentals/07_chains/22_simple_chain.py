from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import time

template = PromptTemplate(
    template = "Generate 5 interesting facts about {topic}"
)

parser = StrOutputParser()

topic = input('Write topic : ')

model = ChatOllama(model='gpt-oss:20b-cloud')

print("Generating response ... ")

start = time.time()

chain = template | model | parser

result = chain.invoke({'topic':topic})

end = time.time()

print(result)

print(f"Response generated in {(end-start):.2f}seconds")

print(type(result))

print(chain.get_graph().draw_ascii())
