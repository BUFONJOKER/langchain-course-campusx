from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()

model = HuggingFaceEndpoint(
    repo_id = "Qwen/Qwen2-7B-instruct",
    task = 'text-generation'
)

chat_model = ChatHuggingFace(llm=model)

messages = [
    SystemMessage(content="You are helpful research assistant"),
    HumanMessage(content="What is Machine Learning?")
]

result = chat_model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)