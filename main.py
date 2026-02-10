import time
from typing import TypedDict, Annotated, Literal, Optional
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_ollama import ChatOllama
from dotenv import load_dotenv

load_dotenv()

class Review(TypedDict):
    summary: Annotated[str, 'Write a 10 words summary of review.']
    sentiment: Annotated[Literal['pos', 'neg'], 'Return sentiment of review either positive, negative or neutral']
    name: Annotated[Optional[str], 'Write name of a reviewer if available']

prompt = '''
    I’ve been using this phone for a month now and it’s been a fantastic experience. 
    The battery life is the standout feature—I can easily get through a full day of heavy use without reaching for a charger. 
    The screen is vibrant and smooth, making it great for watching videos or reading. 
    For the price, you’re getting a premium feel and reliable performance. Highly recommended!
    By MANI
'''

# --- 1. SETUP MODELS ---
# Note: Ensure your HUGGINGFACEHUB_API_TOKEN is in your .env file
hf_llm = HuggingFaceEndpoint(repo_id='Qwen/Qwen2.5-7B-Instruct')
hf_chat_model = ChatHuggingFace(llm=hf_llm)

ollama_model = ChatOllama(model='qwen2.5:7b')

# --- 2. SPEED TEST FUNCTION ---
def check_speed(model_instance, name):
    print(f"--- Running {name} ---")
    structured_model = model_instance.with_structured_output(Review)
    
    start_time = time.perf_counter()
    result = structured_model.invoke(prompt)
    end_time = time.perf_counter()
    
    duration = end_time - start_time
    print(f"Result: {result}")
    print(f"{name} Time: {duration:.2f} seconds\n")
    return duration

# --- 3. EXECUTION ---
# Warning: The first run for Ollama might be slower due to model loading (cold start)
hf_time = check_speed(hf_chat_model, "HuggingFace (Cloud)")
ollama_time = check_speed(ollama_model, "Ollama (Local)")

# --- 4. COMPARISON ---
print(f"Speed Difference: {abs(hf_time - ollama_time):.2f} seconds")
if hf_time < ollama_time:
    print("HuggingFace Cloud was faster.")
else:
    print("Ollama Local was faster.")