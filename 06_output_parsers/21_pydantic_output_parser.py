from langchain_ollama import ChatOllama
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
import time



model = ChatOllama(model='gpt-oss:20b-cloud')

class Person(BaseModel):
    name: str = Field(description='Name of character')
    age: int = Field(gt=18, description='Age of character')
    city: str = Field(description="City of character belongs to")
    comic: str = Field(description='Comic in which character is introduced')

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate.from_template(
    template="Generate name, age, city, comic of fictional character based in {country} \n {format}",
    partial_variables={'format':parser.get_format_instructions()}
)

country = input("Write Country to which Character belong : ")

print("Generating Response ... ")

chain = template | model | parser

start = time.time()

result = chain.invoke({'country':country})

end = time.time()

print(result)

print(f"Response generated in {(end-start):.2f} seconds")
