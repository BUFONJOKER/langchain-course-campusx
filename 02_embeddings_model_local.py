from langchain_huggingface import HuggingFaceEmbeddings
# model will download
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-mpnet-base-v2"
)

# Example usage
vec = embeddings.embed_query("hello world")
docs = embeddings.embed_documents(["first doc", "second doc"])

print(len(vec))