# from transformers import pipeline
import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('OPENAPI_KEY')

class Summarizer:
    def __init__(self):
        openai.api_key = api_key
        self.summarizer = openai

        self.types = {
            'phd': "You are a helpful phd graduate from a top school that helps summarizes transcripts into easily digestiable chunks that can be read in under 5 mintues."
        }

    def summarize(self, text):
        messages = [
            {"role": "system", "content": self.types['phd']},
            {"role": "user", "content": f"Please provide ONLY a accurate summary with nothing else of the following transcript that highlights all the major points:\n\n{text}"}
        ]
        response = openai.chat.completions.create(
            model='gpt-4o-mini',
            messages=messages,
            max_tokens=4096,
            temperature=0.7,
            n=1,
            stop=None,
        )
        print(response)
        summary = response.choices[0].message
        return summary
