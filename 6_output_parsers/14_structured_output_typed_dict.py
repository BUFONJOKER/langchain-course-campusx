from typing import TypedDict, Annotated, Literal, Optional
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_ollama import ChatOllama
from dotenv import load_dotenv

load_dotenv()

class Review(TypedDict):
    summary: Annotated[str,'Write a 10 words summary of review.']
    sentiment: Annotated[Literal['pos','neg'],'Return sentiment of review either positive, negative or neutral']
    name: Annotated[Optional[str], 'Write name of a reviewer if available']


model = HuggingFaceEndpoint(repo_id='Qwen/Qwen2.5-7B-Instruct')

model = ChatHuggingFace(llm=model)



structured_model = model.with_structured_output(Review)

prompt = '''
            I’ve been using this phone for a month now and it’s been a fantastic experience. The battery life is the standout feature—I can easily get through a full day of heavy use without reaching for a charger. The screen is vibrant and smooth, making it great for watching videos or reading. For the price, you’re getting a premium feel and reliable performance. Highly recommended!
            By MANI
        '''
result = structured_model.invoke(prompt)

print(result)
