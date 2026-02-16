from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()

chat_history = [
    SystemMessage(content="You are AI research assistant")
]

model = HuggingFaceEndpoint(
    repo_id = "Qwen/Qwen2-7B-instruct",
    task = "text-generation"
)

model = ChatHuggingFace(llm=model)

while True:
    
    user_input = input("You : ")
    
    chat_history.append(HumanMessage(content=user_input))

    if user_input!='exit':
        result = model.invoke(chat_history)

        print(f"AI: {result.content}")

        chat_history.append(AIMessage(content=result.content))

    else:
        break

print(chat_history)

