# Development Transcript

## Project Goal

Build an AI-powered Message Notification Router capable of classifying incoming messages into:
- Notify
- Digest
- Mute

The system should support text, images, and voice notes while considering user context, historical interactions, and safety.

---

## Development Timeline

### Phase 1 - Environment Setup

- Configured Python environment
- Installed required packages
- Generated and configured Google Gemini API key
- Created `.env` file
- Verified API connectivity

---

### Phase 2 - Dataset Exploration

Explored all provided datasets including:

- messages
- users
- groups
- group_members
- business_accounts
- user_business_history
- message_history
- message_events
- images
- voice_notes
- daily_notification_summary

Studied dataset relationships and identified how contextual information could improve routing decisions.

---

### Phase 3 - Context Retrieval

Implemented a retriever that gathers:

- User information
- Group information
- Business account details
- Historical interactions
- Image paths
- Voice note paths

---

### Phase 4 - Prompt Engineering

Designed structured prompts containing:

- Incoming message
- User context
- Group context
- Business context
- Historical evidence
- Image summaries
- Voice summaries

Configured the AI model to return structured JSON predictions.

---

### Phase 5 - AI Classification

Integrated the Google Gemini API to classify messages into:

- notify
- digest
- mute

The model also predicts:

- message_type
- reason
- confidence

---

### Phase 6 - Media Processing

Added multimodal support:

- Image understanding
- Voice note processing
- Media summaries included in AI prompts

---

### Phase 7 - Historical Evidence

Implemented evidence retrieval to identify similar historical messages and include their IDs in the final output.

---

### Phase 8 - Safety Engine

Implemented rule-based validation to:

- Detect scam keywords
- Detect spam
- Handle heavily forwarded messages
- Respect muted groups
- Normalize prediction labels

---

### Phase 9 - Notification Router

Built a routing pipeline that:

1. Reads incoming messages
2. Retrieves context
3. Processes media
4. Retrieves evidence
5. Calls the AI model
6. Applies safety rules
7. Generates the final prediction

---

### Phase 10 - Output Generation

Generated the final `output.csv` containing:

- message_id
- action
- message_type
- reason
- confidence
- evidence_message_ids

---

## Challenges Encountered

- Google Gemini model version changes
- API rate limits (`RESOURCE_EXHAUSTED`)
- JSON parsing issues
- Media file mapping
- Label normalization
- Retry handling

---

## Final Result

Successfully developed a complete AI-powered notification routing system capable of processing text, image, and voice messages while leveraging contextual retrieval, historical evidence, multimodal AI, and safety rules.