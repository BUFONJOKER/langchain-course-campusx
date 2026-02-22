from langchain_ollama import ChatOllama
from conversion_factor_tool_71 import conversion_factor
from convert_72 import convert
from langchain_core.messages import HumanMessage
import json

llm = ChatOllama(model='qwen3-coder:480b-cloud')

llm_with_tools = llm.bind_tools([conversion_factor, convert])

query = 'What is the conversion factor between USD and PKR, and based on that can you convert 100 USD to PKR'

messages = []

human_message = HumanMessage(query)

messages.append(human_message)

ai_message = llm_with_tools.invoke(messages)

messages.append(ai_message)

for tool_call in ai_message.tool_calls:

    if tool_call['name'] == 'conversion_factor':

        tool_message1 = conversion_factor.invoke(tool_call)

        conversion_rate = json.loads(tool_message1.content)['conversion_rate']

        messages.append(tool_message1)

    if tool_call['name'] == 'convert':
        # make new key in args dictionary as we use inject tool so manually have to give conversion rate
        tool_call['args']['conversion_rate'] = conversion_rate

        tool_message2 = convert.invoke(tool_call)

        messages.append(tool_message2)

result = llm_with_tools.invoke(messages)

print(result.content)