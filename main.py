import pandas as pd

from src.loader import load_all_data
from src.retriever import ContextRetriever
from src.prompt_builder import PromptBuilder
from src.classifier import GeminiClassifier
from src.evidence import EvidenceFinder
from src.media_processor import MediaProcessor
from src.safety import SafetyEngine
from src.router import NotificationRouter


print("Loading data...")

data = load_all_data()

retriever = ContextRetriever(data)
builder = PromptBuilder()
classifier = GeminiClassifier()
evidence = EvidenceFinder(data)
media = MediaProcessor()
safety = SafetyEngine()

router = NotificationRouter(
    retriever,
    builder,
    classifier,
    evidence,
    safety,
    media
)

results = []

messages = data["messages"]

print(f"Processing {len(messages)} messages...\n")

for index, message in messages.iterrows():

    print(f"{index+1}/{len(messages)} : {message['message_id']}")

    try:

        prediction = router.process_message(message)

        results.append(prediction)

    except Exception as e:

        print(e)

        results.append({
            "message_id": message["message_id"],
            "action": "digest",
            "message_type": "unknown",
            "reason": str(e),
            "confidence": 0.5,
            "evidence_message_ids": "none"
        })

output = pd.DataFrame(results)

output = output[
    [
        "message_id",
        "action",
        "message_type",
        "reason",
        "confidence",
        "evidence_message_ids"
    ]
]

output.to_csv("output/output.csv", index=False)

print("\nDone!")
print(output.head())