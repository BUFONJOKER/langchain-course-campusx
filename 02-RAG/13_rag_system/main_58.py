import streamlit as st
from youtube_transcript_loader_50 import load_transcript
from text_splitter_51 import split_transcript
from embeddings_vector_store_52 import build_vector_store
from retriever_53 import build_retriever
from final_chain_56 import answer_question

st.set_page_config(page_title="Youtube Chatbot", page_icon=":robot_face:")

st.title("Youtube Chatbot RAG System with LangChain")

youtube_video_url = st.text_input("Enter a YouTube video URL to load its transcript:")

if "retriever" not in st.session_state:

    st.session_state.retriever = None

if st.button("Load Transcript"):

    if not youtube_video_url:

        st.warning("Please enter a YouTube URL first.")

    else:

        with st.spinner("Loading transcript and building retriever...", 
        show_time=True):

            transcript = load_transcript(youtube_video_url)

            chunks = split_transcript(transcript)

            vector_store = build_vector_store(chunks)

            st.session_state.retriever = build_retriever(vector_store)

        st.success("Transcript loaded. You can ask questions now.")

question = st.text_input("Ask a question about the video:")

if st.button("Submit Question"):

    if not st.session_state.retriever:

        st.warning("Load a transcript first.")

    elif not question:

        st.warning("Please enter a question.")

    else:

        with st.spinner("Generating answer...", show_time=True):

            result = answer_question(question, st.session_state.retriever)

        st.write(result)