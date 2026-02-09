from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embeddings = HuggingFaceEndpointEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")

document = [
    "Salman Ali Agha is the current captain of the Pakistan T20I squad for the 2026 T20 World Cup, leading the team in its opening victory against the Netherlands.",
    "Babar Azam recently returned to the national T20I setup for the 2026 World Cup after fulfilling his franchise commitments with the Sydney Sixers in the Big Bash League.",
    "Shaheen Shah Afridi serves as a core part of the bowling attack for the 2026 T20 World Cup and was recently appointed as Pakistan's ODI captain.",
    "Saim Ayub is a high-ranking T20I all-rounder and left-handed opener known for his aggressive power-hitting at the top of the order.",
    "Naseem Shah remains a spearhead of the Pakistan pace battery, providing crucial speed and accuracy alongside Shaheen Afridi in the 2026 World Cup squad."
]

query = "tell me about Naseem Shah"

document_embeddings = embeddings.embed_documents(texts=document)

query_embeddings = embeddings.embed_query(text=query)

similarities = cosine_similarity([query_embeddings],document_embeddings)[0]

index, score = sorted(list(enumerate(similarities)), reverse=True, key=lambda x:x[1])[0]

print(f"Query : {query}")
print(f"Answer : {document[index]}")
print(f"Similarity Score : {score}")
