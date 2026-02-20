from langchain_community.document_loaders.youtube import TranscriptFormat
from langchain_community.document_loaders import YoutubeLoader


def load_transcript(url: str) -> str:
    loader = YoutubeLoader.from_youtube_url(
        url,
        add_video_info=False,
        transcript_format=TranscriptFormat.CHUNKS,
        chunk_size_seconds=30,
    )

    transcript_list = loader.load()
    return " ".join(t.page_content for t in transcript_list)

