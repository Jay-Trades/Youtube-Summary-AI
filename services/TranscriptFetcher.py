from youtube_transcript_api import YouTubeTranscriptApi
import os
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv('YOUTUBE_API_KEY')

youtube_url = 'https://www.youtube.com/watch?v=qBC6VHhj64c&ab_channel=LukeMadeIt'


class TranscriptFetcher:
    def __init__(self):
        pass

    def get_video_id(self, url):
        print(api_key)
        if 'watch?v' in url:
            parsed_url = youtube_url.split('watch?v=')[1].split("&")[0]
            return parsed_url
        elif "youtu.be/" in url:
            return url.split("youtu.be/")[1].split("?")[0]
        return None


    def get_transcript(self, video_id):
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            # print(transcript)
            transcript_text = ' '.join([n['text'] for n in transcript])
            return transcript_text
        except Exception as e:
            return f"An error has occured: {e}"

    # video_id = get_video_id(youtube_url)
