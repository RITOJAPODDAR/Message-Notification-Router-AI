# AGENTS.md

# Message Notification Router

This file provides guidance for AI coding assistants and contributors working on this repository.

Supported assistants include (but are not limited to):

- ChatGPT
- Claude
- Gemini
- GitHub Copilot
- Cursor
- Windsurf
- Aider
- RooCode
- JetBrains AI Assistant
- Devin

Please read this document before modifying the project.

---

# Project Overview

Message Notification Router is an AI-powered notification management system that determines how incoming messages should be handled.

For every incoming message, the system predicts one of three actions:

- **notify** — interrupt the user immediately
- **digest** — include the message in a later summary
- **mute** — suppress low-value, repetitive, spam, or unsafe content

The project supports multimodal inputs including:

- Text messages
- Image messages
- Voice notes

Predictions are personalized using user history, group context, business relationships, historical interactions, and media understanding.

---

# Repository Structure

```
dataset/
│
├── messages.csv
├── users.csv
├── groups.csv
├── group_members.csv
├── business_accounts.csv
├── user_business_history.csv
├── message_history.csv
├── message_events.csv
├── images.csv
├── voice_notes.csv
├── daily_notification_summary.csv
└── media/

src/
│
├── loader.py
├── retriever.py
├── prompt_builder.py
├── classifier.py
├── evidence.py
├── media_processor.py
├── safety.py
└── router.py

output/
main.py
README.md
requirements.txt
```

---

# System Pipeline

The project follows the pipeline below:

```
Incoming Message
        │
        ▼
Dataset Loader
        │
        ▼
Context Retrieval
        │
        ▼
Historical Evidence Retrieval
        │
        ▼
Media Processing
(Image / Voice)
        │
        ▼
Prompt Builder
        │
        ▼
AI Classification
        │
        ▼
Safety Engine
        │
        ▼
Notification Router
        │
        ▼
output/output.csv
```

---

# Expected Output

The application generates:

```
output/output.csv
```

with the following columns:

```
message_id
action
message_type
reason
confidence
evidence_message_ids
```

Allowed actions:

- notify
- digest
- mute

Allowed message types:

- personal
- urgent
- event
- payment
- business_update
- promotion
- greeting
- forward
- spam
- scam
- unknown

---

# Development Guidelines

When contributing to this project:

- Preserve the existing project structure whenever possible.
- Prefer extending existing modules over creating duplicate functionality.
- Keep the routing pipeline modular.
- Ensure generated output always follows the required schema.
- Use environment variables for API keys and secrets.
- Avoid hardcoding dataset-specific values.
- Keep changes deterministic where practical.

---

# Coding Principles

- Write readable and maintainable code.
- Prefer descriptive variable and function names.
- Keep functions focused on a single responsibility.
- Handle API failures gracefully.
- Include meaningful error messages.
- Minimize unnecessary API calls.
- Preserve compatibility with existing modules.

---

# Running the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python main.py
```

The generated predictions will be saved to:

```
output/output.csv
```

---

# Future Improvements

Potential enhancements include:

- Intelligent caching
- Confidence calibration
- Batch inference
- Improved voice transcription
- Faster multimodal processing
- Enhanced scam detection
- Local fallback models
- Model benchmarking
- Dashboard for prediction visualization

---

# Notes for AI Coding Assistants

When making changes:

- Maintain compatibility with the current routing pipeline.
- Avoid introducing breaking changes without clear justification.
- Preserve the output schema.
- Keep modules independent and reusable.
- Favor incremental improvements over large-scale rewrites unless explicitly requested.
