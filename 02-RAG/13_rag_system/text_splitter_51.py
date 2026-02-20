from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_transcript(transcript: str):
	text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
	return text_splitter.create_documents([transcript])
