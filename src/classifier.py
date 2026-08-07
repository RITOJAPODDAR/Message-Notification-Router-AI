import os
import json
import time

from dotenv import load_dotenv
from google import genai

load_dotenv()


class GeminiClassifier:

    def __init__(self):

        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

    def classify(self, prompt):

        for attempt in range(3):

            try:

                response = self.client.models.generate_content(
                    model="gemini-3.5-flash",
                    contents=prompt
                )

                text = response.text.strip()

                # Remove markdown if Gemini returns it
                text = text.replace("```json", "")
                text = text.replace("```", "")
                text = text.strip()

                return json.loads(text)

            except Exception as e:

                print(f"Retry {attempt + 1}: {e}")

                time.sleep(2)

        return {
            "action": "digest",
            "message_type": "unknown",
            "reason": "Classification failed after retries.",
            "confidence": 0.5
        }