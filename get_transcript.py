from youtube_transcript_api import YouTubeTranscriptApi

def getTranscript():
    transcript_list = YouTubeTranscriptApi.list_transcripts("xGXPc7KL5xA")
    transcript = transcript_list.find_generated_transcript(['fr'])
    text = transcript.fetch()

    return len(text)
    
print(getTranscript())