from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
# load_dotenv()

# model = HuggingFaceEndpoint(
#     repo_id='Qwen/Qwen2-7B-instruct',task='text-generation'
# )

# model = ChatHuggingFace(llm=model)
model = ChatOllama(model='gpt-oss:20b-cloud') 

template_1 = PromptTemplate.from_template(
    template="Write detailed report on {topic}"
)

topic = 'Black Hole'

prompt_1 = template_1.invoke({'topic':topic})

result = model.invoke(prompt_1)

template_2 = PromptTemplate.from_template(
    template="Write 50 words summary of the following text. /n {text}"
)

prompt_2 = template_2.invoke({'text':result.content})

result_2 = model.invoke(prompt_2)

print(result_2.content)