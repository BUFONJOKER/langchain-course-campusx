from langchain.tools import tool
from dotenv import load_dotenv
import requests
import os

load_dotenv()

EXCHANGE_RATE_API_KEY = os.getenv('EXCHANGE_RATE_API_KEY')

@tool
def conversion_factor(base_currency: str, target_currency: str) -> float:
    '''
    this function fetches currency conversion factor between base currency and target currency
    '''

    url = f"https://v6.exchangerate-api.com/v6/{EXCHANGE_RATE_API_KEY}/pair/{base_currency}/{target_currency}"

    response = requests.get(url)

    return response.json()