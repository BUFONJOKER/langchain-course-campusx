from langchain.tools import tool
from langchain_ollama import ChatOllama

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

llm = ChatOllama(model='gpt-oss:120b-cloud')

llm_with_tools = llm.bind_tools([multiply])

print(llm_with_tools)

