from langchain_community.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()

result = search_tool.invoke("top news in pakistan today")

print(result)

print()

print(search_tool.name)
print(search_tool.description)
print(search_tool.args)