from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
import time

load_dotenv()

# model = HuggingFaceEndpoint(
#     repo_id='Qwen/Qwen2-7B-instruct',task='text-generation'
# )

# model = ChatHuggingFace(llm=model)

model = ChatOllama(model='gpt-oss:20b-cloud') 

template_1 = PromptTemplate.from_template(
    template="Write detailed report on {topic}"
)

topic = input("Write Topic : ")

template_2 = PromptTemplate.from_template(
    template="Write 50 words summary of the following text. /n {text}"
)

parser = StrOutputParser()

print("Generating Summary ...")

start = time.time()

chain = template_1 | model | parser | template_2 | model | parser

result = chain.invoke({'topic':topic})

print(result)

end = time.time()

print(f"Summary generated in {end - start} seconds")