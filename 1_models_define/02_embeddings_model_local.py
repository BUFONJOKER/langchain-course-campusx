from langchain_huggingface import HuggingFaceEmbeddings

# Model will download on first run.
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-mpnet-base-v2"
)

# Example usage: query embedding and batch document embeddings.
vec = embeddings.embed_query("hello world")
docs = embeddings.embed_documents(["first doc", "second doc"])

print(len(vec))