from langchain.tools import tool

@tool
def add_numbers(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b

@tool
def multiply_numbers(a: int, b: int) -> int:
    """Multiply two numbers together."""
    return a * b

class MathToolkit:
    """A toolkit for performing basic math operations."""

    def get_tools(self):
        """Return the tools in the toolkit."""
        return [add_numbers, multiply_numbers]

math_toolkit = MathToolkit()
print(math_toolkit.get_tools())