# Message Notification Router

## Overview

Message Notification Router is an AI-powered system that intelligently decides how incoming messages should be handled.

Instead of notifying users for every message, the system analyzes the content, user context, historical interactions, business relationships, and media attachments to determine whether a message should:

- Notify immediately
- Be included in a later digest
- Be muted because it is low priority, spam, or suspicious

The project supports multimodal messages including text, images, and voice notes.

---

## Features

- AI-powered message classification
- Personalized notification routing
- Image understanding
- Voice note understanding
- Historical evidence retrieval
- User context retrieval
- Business verification checks
- Group context analysis
- Safety engine for scam and spam detection
- Automatic output generation

---

## Project Structure

```
dataset/
src/
output/
main.py
requirements.txt
README.md
```

---

## Technologies Used

- Python
- Google Gemini API
- Pandas

---

## How It Works

1. Load incoming messages and contextual datasets.
2. Retrieve user, business, and group information.
3. Analyze media content when images or voice notes are present.
4. Retrieve similar historical messages as evidence.
5. Generate an AI prediction.
6. Apply safety rules to prevent unsafe notifications.
7. Save the final routing decisions to `output/output.csv`.

---

## Running the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python main.py
```

The generated predictions will be saved in:

```
output/output.csv
```

---

## Future Improvements

- Smarter caching to reduce AI API calls
- Better confidence calibration
- Faster batch processing
- Improved voice transcription
- Enhanced scam detection using hybrid AI and rule-based reasoning