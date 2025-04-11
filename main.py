from services.TranscriptFetcher import TranscriptFetcher 
from services.Summarizer import Summarizer
import os
os.environ['CUDA_LAUNCH_BLOCKING'] = '1'

youtube_url = 'https://www.youtube.com/watch?v=qBC6VHhj64c&ab_channel=LukeMadeIt'


def main():
    transcriptFetcher = TranscriptFetcher()
    summarizer_obj = Summarizer()
    video_id = transcriptFetcher.get_video_id(youtube_url)
    transcript = transcriptFetcher.get_transcript(video_id)
    print(len(transcript))
    summary = summarizer_obj.summarize(transcript)
    print(summary)

if __name__=="__main__":
    main()

