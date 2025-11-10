from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
    

# fetch transcript
def fetch_youtube_transcript(video_id: str) -> str:
    try:
        transcript_snippets = YouTubeTranscriptApi().fetch(video_id, languages=['en','hi'])
        text = " ".join(snippet.text for snippet in transcript_snippets)
        return text
    except TranscriptsDisabled:
        return "No captions available for this video."
    
