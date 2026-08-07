# 📩 Message Notification Router AI

An AI-powered notification routing system that intelligently prioritizes incoming text, image, and voice messages using multimodal reasoning, contextual retrieval, historical evidence, and rule-based safety checks.

---

## 📖 Overview

Modern messaging applications generate a large number of notifications every day. Treating every message equally can overwhelm users, causing important messages to be missed while low-value or suspicious messages create unnecessary interruptions.

**Message Notification Router AI** analyzes incoming messages and decides whether they should:

- 🔔 **Notify** – Important enough to interrupt the user immediately.
- 📋 **Digest** – Useful but can be shown later.
- 🔇 **Mute** – Spam, scams, repetitive, or low-priority messages.

The system combines AI-powered reasoning with contextual retrieval and safety rules to make personalized notification decisions.

---

## ✨ Features

- 🤖 AI-powered message classification
- 💬 Text message understanding
- 🖼️ Image understanding using Gemini Vision
- 🎙️ Voice note understanding
- 👤 Personalized user context retrieval
- 👥 Group context analysis
- 🏢 Business account verification
- 📚 Historical message evidence retrieval
- 🛡️ Rule-based spam and scam detection
- 📊 Confidence scoring
- 📁 Automatic CSV output generation

---

## 🏗️ System Architecture

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
 (Images / Voice Notes)
        │
        ▼
 Prompt Builder
        │
        ▼
 Gemini AI Classification
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

## 📂 Project Structure

```
Message-Notification-Router-AI/
│
├── dataset/
│   ├── messages.csv
│   ├── users.csv
│   ├── groups.csv
│   ├── group_members.csv
│   ├── business_accounts.csv
│   ├── user_business_history.csv
│   ├── message_history.csv
│   ├── message_events.csv
│   ├── images.csv
│   ├── voice_notes.csv
│   ├── daily_notification_summary.csv
│   └── media/
│       ├── images/
│       └── audio/
│
├── src/
│   ├── classifier.py
│   ├── evidence.py
│   ├── loader.py
│   ├── media_processor.py
│   ├── prompt_builder.py
│   ├── retriever.py
│   ├── router.py
│   └── safety.py
│
├── output/
│   └── output.csv
│
├── main.py
├── requirements.txt
├── .env.example
├── README.md
└── AGENTS.md
```

---

## ⚙️ Technologies Used

- Python
- Google Gemini API
- Pandas
- Python Dotenv

---

## 🚀 How It Works

1. Load incoming messages and supporting datasets.
2. Retrieve user, group, and business context.
3. Analyze attached images and voice notes.
4. Retrieve similar historical messages.
5. Build a structured prompt for the AI model.
6. Generate routing predictions using Gemini.
7. Apply safety and validation rules.
8. Save the final predictions to `output/output.csv`.

---

## 📋 Output Format

The generated `output.csv` contains the following fields:

| Column | Description |
|---------|-------------|
| message_id | Unique message identifier |
| action | notify, digest, or mute |
| message_type | Predicted message category |
| reason | Human-readable explanation |
| confidence | Confidence score (0–1) |
| evidence_message_ids | Related historical message IDs |

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/RITOJAPODDAR/Message-Notification-Router-AI.git
cd Message-Notification-Router-AI
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

Run the project:

```bash
python main.py
```

The generated predictions will be available in:

```
output/output.csv
```

---

## 📈 Future Improvements

- Batch inference for faster processing
- Intelligent caching of AI responses
- Improved confidence calibration
- Advanced voice transcription
- Local fallback models
- Enhanced scam detection
- Web dashboard for visualization
- Real-time notification routing

---

## 🤝 Contributing

Contributions are welcome!

If you'd like to improve the project:

1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Open a Pull Request.

---

## 📄 License

This project is released under the MIT License.

---

## 👨‍💻 Author

**Ritoja Poddar**


AI • Python • Web Development • Machine Learning

GitHub: https://github.com/RITOJAPODDAR
