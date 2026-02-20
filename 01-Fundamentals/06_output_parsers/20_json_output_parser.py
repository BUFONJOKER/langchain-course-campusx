from langchain_ollama import ChatOllama
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
import time

start = time.time()

model = ChatOllama(model='gpt-oss:20b-cloud')

parser = JsonOutputParser()

template = PromptTemplate.from_template(
    template="Give me name, age, city, comic of fictional charachter \n {format}",
    partial_variables={'format': parser.get_format_instructions()}
)


chain = template | model | parser

final_output = chain.invoke({})

end = time.time()

print(final_output)

print(f"Name: {final_output['name']}, Age: {final_output['age']}, City: {final_output['city']}, Comic: {final_output['comic']}")

print(f"Time taken to generate response : {end-start} seconds")