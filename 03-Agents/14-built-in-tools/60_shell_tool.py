from langchain_community.tools import ShellTool

command_tool = ShellTool()

result = command_tool.invoke('ollama ls')

print(result)