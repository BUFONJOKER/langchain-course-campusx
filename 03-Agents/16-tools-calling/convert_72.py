from langchain.tools import InjectedToolArg, tool
from typing import Annotated

@tool
def convert(base_currency_value: int, conversion_rate: Annotated[float, InjectedToolArg]) -> float:

    '''
    given a currency conversion rate this function calculates the target currency value from a given base currency value
    '''

    return base_currency_value * conversion_rate