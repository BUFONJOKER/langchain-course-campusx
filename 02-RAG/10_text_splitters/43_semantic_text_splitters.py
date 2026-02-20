from langchain_text_splitters import CharacterTextSplitter
import streamlit as st

st.title("Semantic Based Text Splitter")

text = '''

    Farmers are the unsung architects of civilization, laboring through unpredictable seasons to ensure global food security.The Pakistan Super League has evolved far beyond a mere cricket tournament; it is a vibrant cultural phenomenon that unites a diverse nation through the spirit of sport.

    Terrorism remains one of the most complex and devastating challenges to international peace and security, driven by radical ideologies and systemic grievances. It seeks to undermine the stability of sovereign states by spreading fear and targeting the innocent, leaving behind a trail of psychological and physical destruction.
'''


# Token-based with cl100k_base (GPT-4 tokenizer)
token_splitter = CharacterTextSplitter.from_tiktoken_encoder(
    encoding_name="cl100k_base",
    chunk_size=300,       # ~300 tokens safe for most models
    chunk_overlap=50
)

docs = token_splitter.split_text(text)

st.write(docs)