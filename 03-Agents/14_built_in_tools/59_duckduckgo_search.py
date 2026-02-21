from langchain_community.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()

result = search_tool.invoke("icc t20 world cup 2026 pak vs nz")

print(result)