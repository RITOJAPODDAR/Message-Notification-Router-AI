import re


class SafetyEngine:

    def __init__(self):

        self.scam_keywords = [
            "lottery",
            "won",
            "winner",
            "claim",
            "claim now",
            "click here",
            "verify your account",
            "verify account",
            "kyc",
            "otp",
            "password",
            "bank blocked",
            "gift card",
            "crypto",
            "investment",
            "earn money",
            "free money",
            "urgent payment",
            "account suspended",
            "limited offer"
        ]

    def apply(self, message_row, context, prediction):

        text = str(message_row["message_text"]).lower()

        # Rule 1: Scam keywords
        for word in self.scam_keywords:

            if word in text:

                prediction["action"] = "mute"
                prediction["message_type"] = "scam"

                prediction["reason"] = (
                    "Message contains suspicious scam-like keywords."
                )

                prediction["confidence"] = max(
                    prediction["confidence"],
                    0.97
                )

                return prediction

        # Rule 2: Very highly forwarded
        if message_row["forwarded_count"] >= 10:

            prediction["action"] = "digest"

            prediction["reason"] += (
                " Message is heavily forwarded."
            )

            prediction["confidence"] = min(
                prediction["confidence"],
                0.80
            )

        # Rule 3: Muted group
        if len(context["group_member"]) > 0:

            member = context["group_member"][0]

            if member["group_muted_by_user"] == 1:

                if prediction["action"] == "notify":

                    prediction["action"] = "digest"

                    prediction["reason"] += (
                        " User has muted this group."
                    )

        # Rule 4: Business reports
        if len(context["business"]) > 0:

            business = context["business"][0]

            if business["user_reports_30d"] >= 20:

                prediction["action"] = "mute"

                prediction["message_type"] = "spam"

                prediction["reason"] = (
                    "Business has many recent user reports."
                )

                prediction["confidence"] = 0.95
        

        # ----- Normalize action -----

        valid_actions = ["notify", "digest", "mute"]

        if prediction["action"] not in valid_actions:

            if prediction["action"] == "ignore":
                prediction["action"] = "mute"
            else:
                prediction["action"] = "digest"

        # ----- Normalize message type -----

        valid_types = [
            "personal",
            "urgent",
            "event",
            "payment",
            "business_update",
            "promotion",
            "greeting",
            "forward",
            "spam",
            "scam",
            "unknown"
        ]

        if prediction["message_type"] not in valid_types:
            prediction["message_type"] = "unknown"



        return prediction