from pydantic import BaseModel, Field
from langchain.tools import tool

class MultiplyInput(BaseModel):
    a: int = Field(description='The first number to multiply')
    b: int = Field(description='The second number to multiply')

@tool(args_schema=MultiplyInput)
def multiply(a: int, b: int) -> int:
    """Multiplies two numbers together."""
    return a*b


result = multiply.invoke({'a': 5, 'b': 10})

print(result)

print(multiply.name)

print(multiply.description)