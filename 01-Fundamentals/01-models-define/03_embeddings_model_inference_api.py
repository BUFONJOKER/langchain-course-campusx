from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv

# Load environment variables for the Hugging Face token.
load_dotenv()

# Use the hosted inference API for embeddings.
embeddings = HuggingFaceEndpointEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")

text = "hello"
# create an embedding for the query text.
vec = embeddings.embed_query(text)

print(len(vec))