from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "mistralai/Mistral-7B-Instruct-v0.2",
    task = "text-generation"
)
try:
    print("Initializing the model...")

    model = ChatHuggingFace(llm=llm)

    response = model.invoke("What is the capital of France?")

    print(response.content)
except Exception as e:
    print(f"An error occurred: {e}")