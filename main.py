from langsmith import Client

# Initialize the new client
client = Client()

# Use the new pull_prompt method (replaces pull)
prompt = client.pull_prompt("hwchase17/react")

print("Successfully pulled prompt using LangSmith SDK!")