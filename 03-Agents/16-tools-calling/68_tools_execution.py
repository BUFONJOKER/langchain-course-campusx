from langchain.tools import tool
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, ToolMessage
@tool
def multiply(a: int, b:int) -> int:
    """Multiply two numbers"""
    return a * b

llm = ChatOllama(model='gpt-oss:120b-cloud')

llm_with_tools = llm.bind_tools([multiply])

query = HumanMessage('Multiply 12 with 16')

messages = [query]

llm_response = llm_with_tools.invoke(messages)

messages.append(llm_response)

tool_result = multiply.invoke(llm_response.tool_calls[0])

messages.append(tool_result)

result = llm_with_tools.invoke(messages)

print(result.content)
