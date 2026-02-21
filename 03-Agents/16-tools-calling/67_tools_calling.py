from langchain_ollama import ChatOllama
from langchain.tools import tool

@tool
def multiply(a: int, b:int) -> int:
    """Multiply two numbers"""
    return a * b

llm = ChatOllama(model='gpt-oss:120b-cloud')

llm_with_tools = llm.bind_tools([multiply])

result = llm_with_tools.invoke("Mutliply 12 with 14")

print(result.tool_calls)