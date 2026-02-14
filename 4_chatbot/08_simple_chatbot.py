from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()

model = HuggingFaceEndpoint(
    repo_id='Qwen/Qwen2-7B-instruct',
    task='text-generation',
    )

chatbot = ChatHuggingFace(llm=model)

chat_history = []

while True:
    user = input("You : ")
    chat_history.append(user)
    if user!='exit':
        response = chatbot.invoke(chat_history)
        chat_history.append(response.content)
        print("AI : ",response.content)
    else:
        break