from embeddings_vector_store_52 import vector_store

retriever = vector_store.as_retriever(
    search_type="similarity", search_kwargs={"k": 3}
)