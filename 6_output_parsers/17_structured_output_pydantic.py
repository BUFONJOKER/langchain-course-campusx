from typing import TypedDict, Annotated, Literal, Optional
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()

class Review(BaseModel):

    summary: str = Field(description='Write a 10 words summary of review.')

    sentiment: Literal['pos','neg'] = Field(description='Return sentiment of review either positive, negative or neutral')

    name: Optional[str] = Field(default='Anonymous', description='Write name of a reviewer if available')

model = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct"
)

model = ChatHuggingFace(llm=model)

structured_model = model.with_structured_output(Review, method='json_mode')

prompt = '''
            I’ve been using this phone for a month now and it’s been a fantastic experience. The battery life is the standout feature—I can easily get through a full day of heavy use without reaching for a charger. The screen is vibrant and smooth, making it great for watching videos or reading. For the price, you’re getting a premium feel and reliable performance. Highly recommended!
            By MANI
        '''
result = structured_model.invoke(prompt)

print(result)
