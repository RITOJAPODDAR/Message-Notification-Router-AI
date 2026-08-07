import json
import pandas as pd


class PromptBuilder:

    def __init__(self):
        self.sample = pd.read_csv("dataset/sample_messages.csv")

    def build_examples(self):

        examples = ""

        # Use first 5 sample messages
        for _, row in self.sample.head(5).iterrows():

            examples += f"""
Example

Message:
{row['message_text']}

Action:
{row['action']}

Message Type:
{row['message_type']}

Reason:
{row['reason']}

Confidence:
{row['confidence']}

Evidence:
{row['evidence_message_ids']}

-----------------------------------
"""

        return examples

    def build_prompt(self, context):

        examples = self.build_examples()

        prompt = f"""
You are an expert AI Notification Router for WhatsApp.

Your job is to classify incoming messages exactly like the examples below.

=========================
REFERENCE EXAMPLES
=========================

{examples}

=========================
CURRENT MESSAGE
=========================

{json.dumps(context['message'], indent=2)}

=========================
USER
=========================

{json.dumps(context['user'], indent=2)}

=========================
MESSAGE HISTORY
=========================

{json.dumps(context['history'], indent=2)}


=========================
IMAGE SUMMARY
=========================

{context.get("image_summary", "")}

=========================
VOICE SUMMARY
=========================

{context.get("voice_summary", "")}

=========================
GROUP
=========================

{json.dumps(context['group'], indent=2)}

=========================
GROUP MEMBERSHIP
=========================

{json.dumps(context['group_member'], indent=2)}

=========================
BUSINESS
=========================

{json.dumps(context['business'], indent=2)}

=========================
BUSINESS HISTORY
=========================

{json.dumps(context['business_history'], indent=2)}

=========================
NOTIFICATION SUMMARY
=========================

{json.dumps(context['daily_summary'], indent=2)}

=========================

Rules:

1. Think like the reference examples.
2. Personalize using user history.
3. Consider scams and phishing.
4. Consider repeated messages.
5. Consider business trust.
6. Consider muted groups.
7. Consider image and voice summaries if provided.
8. Return ONLY valid JSON.
9. Do NOT invent labels.

Allowed action values:
- notify
- digest
- mute

Allowed message_type values:
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

Output Format

{{
"action":"",
"message_type":"",
"reason":"",
"confidence":0.0
}}
"""

        return prompt