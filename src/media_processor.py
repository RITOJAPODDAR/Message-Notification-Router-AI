import os
from dotenv import load_dotenv
from google import genai

load_dotenv()


class MediaProcessor:

    def __init__(self):

        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

    def process_image(self, image_path):

        try:

            uploaded = self.client.files.upload(
                file=image_path
            )

            response = self.client.models.generate_content(
                model="gemini-3.5-flash",
                contents=[
                    uploaded,
                    """
Describe this WhatsApp image in 2-3 sentences.

Focus on:
- Is it a promotion?
- Is it a payment reminder?
- Is it an event?
- Is it suspicious?
- Is it urgent?
"""
                ]
            )

            return response.text

        except Exception as e:

            return f"Image processing failed: {e}"

    def process_audio(self, audio_path):

        try:

            uploaded = self.client.files.upload(
                file=audio_path
            )

            response = self.client.models.generate_content(
                model="gemini-3.5-flash",
                contents=[
                    uploaded,
                    """
Transcribe this voice note and summarize it briefly.
Mention if it sounds urgent, promotional, payment-related, or suspicious.
"""
                ]
            )

            return response.text

        except Exception as e:

            return f"Audio processing failed: {e}"