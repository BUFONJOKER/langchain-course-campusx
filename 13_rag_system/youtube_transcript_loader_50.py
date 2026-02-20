from langchain_community.document_loaders.youtube import TranscriptFormat
from langchain_community.document_loaders import YoutubeLoader

loader = YoutubeLoader.from_youtube_url(
    "https://youtu.be/Gfr50f6ZBvo?si=Z9PyEBMC835be5Rb",
    add_video_info=False,
    transcript_format=TranscriptFormat.CHUNKS,
    chunk_size_seconds=30,
)
transcript_list = loader.load()

transcript = ' '.join([t.page_content for t in transcript_list])

