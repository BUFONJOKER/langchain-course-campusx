from langchain_community.tools import ShellTool

command_tool = ShellTool()

result = command_tool.invoke('ollama ls')

print(result)

print()

print(command_tool.name)
print(command_tool.description)
print(command_tool.args)