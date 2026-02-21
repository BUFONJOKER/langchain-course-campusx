import time
from typing import TypedDict, Annotated, Literal, Optional
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_ollama import ChatOllama
from dotenv import load_dotenv

load_dotenv()

# Using a Class-based approach often helps local models follow instructions better
class Review(TypedDict):
    summary: Annotated[str, 'Write a 10 words summary of review.']
    sentiment: Annotated[Literal['pos', 'neg'], 'Return sentiment of review either positive, negative or neutral']
    name: Annotated[Optional[str], 'Write name of a reviewer if available']

# We add a specific instruction to the prompt to stop the "chatter"
review_text = '''
    I’ve been using this phone for a month now and it’s been a fantastic experience. 
    The battery life is the standout feature—I can easily get through a full day of heavy use without reaching for a charger. 
    The screen is vibrant and smooth, making it great for watching videos or reading. 
    For the price, you’re getting a premium feel and reliable performance. Highly recommended!
    By MANI
'''

# Force the prompt to be an instruction
prompt = f"Extract the details from this review into JSON format: {review_text}"

# --- 1. SETUP MODELS ---
hf_llm = HuggingFaceEndpoint(repo_id='Qwen/Qwen2.5-7B-Instruct')
hf_chat_model = ChatHuggingFace(llm=hf_llm)

# FIX: Added format="json" and a lower temperature to stop the model from talking too much
ollama_model = ChatOllama(
    model='deepseek-v3.1:671b-cloud',
    format="json",
    temperature=0
)

# --- 2. SPEED TEST FUNCTION ---
def check_speed(model_instance, name):
    print(f"--- Running {name} ---")
    
    # We tell the model to be strict about the Review schema
    structured_model = model_instance.with_structured_output(Review)
    
    start_time = time.perf_counter()
    try:
        result = structured_model.invoke(prompt)
        end_time = time.perf_counter()
        duration = end_time - start_time
        print(f"Result: {result}")
        print(f"{name} Time: {duration:.2f} seconds\n")
        return duration
    except Exception as e:
        print(f"Error in {name}: {e}")
        return 0

# --- 3. EXECUTION ---
hf_time = check_speed(hf_chat_model, "HuggingFace (Cloud)")
ollama_time = check_speed(ollama_model, "Ollama (Local)")

# --- 4. COMPARISON ---
if hf_time and ollama_time:
    print(f"Speed Difference: {abs(hf_time - ollama_time):.2f} seconds")
    if hf_time < ollama_time:
        print("HuggingFace Cloud was faster.")
    else:
        print("Ollama Local was faster.")
        