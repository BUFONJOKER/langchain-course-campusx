from langchain_ollama import ChatOllama
from langchain.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from dotenv import load_dotenv
from langchain.agents import create_agent
import requests
import os
from langsmith import Client

load_dotenv()

WEATHER_STACK_API_KEY = os.getenv('WEATHER_STACK_API_KEY')

llm = ChatOllama(model='qwen3.5:cloud')

search_tool = DuckDuckGoSearchRun()

@tool
def get_weather_data(city: str) -> str:
    '''
    This function return weather data of given of city provided
    '''

    url = f"http://api.weatherstack.com/current?access_key={WEATHER_STACK_API_KEY}&query={city}"

    response = requests.get(url)

    return response.json()

tools = [search_tool, get_weather_data]

# Initialize the new client
client = Client()

# Use the new pull_prompt method (replaces pull)
prompt_template = client.pull_prompt("hwchase17/react")

# Partial with tools (critical!)
prompt_partial = prompt_template.partial(
    tools="\n".join([f"{t.name}: {t.description}" for t in tools]),
    tool_names=", ".join([t.name for t in tools])
)

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=prompt_partial.template  # Use .template after partial

)

# Invoke
result = agent.invoke({
    "messages": [{"role": "user", "content": "Weather in Chishtian,Punjab,Pakistan and search LangChain?"}]
})
print(result["messages"][-1].content)