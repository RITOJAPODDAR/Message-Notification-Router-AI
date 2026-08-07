from difflib import SequenceMatcher


class EvidenceFinder:

    def __init__(self, data):
        self.history = data["message_history"]

    def find(self, message_row, top_k=2):

        user_history = self.history[
            self.history["user_id"] == message_row["user_id"]
        ]

        scores = []

        current_text = str(message_row["message_text"]).lower()

        for _, row in user_history.iterrows():

            score = 0

            # Same business
            if (
                str(message_row["business_id"]) != "nan"
                and message_row["business_id"] == row["business_id"]
            ):
                score += 5

            # Same group
            if (
                str(message_row["group_id"]) != "nan"
                and message_row["group_id"] == row["group_id"]
            ):
                score += 5

            # Same sender
            if (
                str(message_row["sender_user_id"]) != "nan"
                and message_row["sender_user_id"] == row["sender_user_id"]
            ):
                score += 3

            # Same conversation type
            if message_row["conversation_type"] == row["conversation_type"]:
                score += 2

            # Similar text
            history_text = str(row["message_text"]).lower()

            similarity = SequenceMatcher(
                None,
                current_text,
                history_text
            ).ratio()

            score += similarity * 10

            scores.append((score, row["message_id"]))

        scores.sort(reverse=True)

        evidence = [m for _, m in scores[:top_k]]

        if len(evidence) == 0:
            return "none"

        return ";".join(evidence)