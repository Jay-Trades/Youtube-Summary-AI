from flask import Flask, request, jsonify
from TranscriptFetcher import TranscriptFetcher
from Summarizer import Summarizer
import os

os.environ['CUDA_LAUNCH_BLOCKING'] = '1'

app = Flask(__name__)


# Initialize objects
transcriptFetcher = TranscriptFetcher()
summarizer_obj = Summarizer()

@app.route('/', methods=['POST'])
def summarize_video():
    # Get the URL from the POST request
    data = request.get_json()
    youtube_url = data.get('url')

    if not youtube_url:
        return jsonify({'error': 'URL is required'}), 400

    try:
        # Fetch transcript and summarize
        video_id = transcriptFetcher.get_video_id(youtube_url)
        transcript = transcriptFetcher.get_transcript(video_id)
        summary = summarizer_obj.summarize(transcript)
        return jsonify({'summary': summary})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)