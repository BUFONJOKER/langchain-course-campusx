from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

# Load environment variables for the Hugging Face token.
load_dotenv()

# Configure the text-generation endpoint.
llm = HuggingFaceEndpoint(
    repo_id = "mistralai/Mistral-7B-Instruct-v0.2",
    task = "text-generation"
)
try:
    print("Initializing the model...")

    # Wrap the endpoint with a chat interface.
    model = ChatHuggingFace(llm=llm)
    # sending a message to the model and getting the response.
    response = model.invoke("What is the capital of France?")

    print(response.content)
except Exception as e:
    print(f"An error occurred: {e}")