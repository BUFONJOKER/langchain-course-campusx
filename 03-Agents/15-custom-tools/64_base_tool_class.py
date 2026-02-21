from langchain.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

class MultiplyInput(BaseModel):
    a: int = Field(description='The first number to multiply')
    b: int = Field(description='The second number to multiply')

class MultiplyTool(BaseTool):
    name: str = "multiply"
    description: str = "Multiply two numbers together"

    args_schema: Type[BaseModel] = MultiplyInput

    def _run(self, a: int, b: int) -> int:
        return a * b

multiply_tool = MultiplyTool()

result = multiply_tool.invoke({'a':10, 'b':2})

print(result)

print(f"MultiplyTool name: {multiply_tool.name}")
print(f"MultiplyTool description: {multiply_tool.description}")
print(f"MultiplyTool args_schema: {multiply_tool.args_schema}")
print(f"MultiplyTool args method: {multiply_tool.args}")