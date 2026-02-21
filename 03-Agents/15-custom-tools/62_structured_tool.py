from langchain_core.tools import StructuredTool 
from pydantic import BaseModel, Field

class MultiplyInput(BaseModel):
    a: int = Field(description='The first number to multiply')
    b: int = Field(description='The second number to multiply')

def multiply(a: int, b: int) -> int:
    """Multiplies two numbers together."""
    return a*b

multiply_tool = StructuredTool.from_function(
    func=multiply,
    args_schema=MultiplyInput,
    name='multiply',
    description='Multiplies two numbers together'
)

result = multiply_tool.invoke({'a': 5, 'b': 10})
print(result)