class ContextRetriever:

    def __init__(self, data):

        self.data = data

    def get_context(self, message_row):

        context = {}

        user_id = message_row["user_id"]

        context["message"] = message_row.to_dict()

        context["user"] = self.data["users"][
            self.data["users"]["user_id"] == user_id
        ].to_dict("records")

        context["history"] = self.data["message_history"][
            self.data["message_history"]["user_id"] == user_id
        ].tail(10).to_dict("records")

        # Group information
        if "group_id" in message_row and str(message_row["group_id"]) != "nan":

            gid = message_row["group_id"]

            context["group"] = self.data["groups"][
                self.data["groups"]["group_id"] == gid
            ].to_dict("records")

            context["group_member"] = self.data["group_members"][
                (self.data["group_members"]["group_id"] == gid) &
                (self.data["group_members"]["user_id"] == user_id)
            ].to_dict("records")

        else:

            context["group"] = []

            context["group_member"] = []

        # Business information
        if "business_id" in message_row and str(message_row["business_id"]) != "nan":

            bid = message_row["business_id"]

            context["business"] = self.data["business_accounts"][
                self.data["business_accounts"]["business_id"] == bid
            ].to_dict("records")

            context["business_history"] = self.data["user_business_history"][
                (self.data["user_business_history"]["business_id"] == bid) &
                (self.data["user_business_history"]["user_id"] == user_id)
            ].to_dict("records")

        else:

            context["business"] = []

            context["business_history"] = []

        # Notification Load

        context["daily_summary"] = self.data["daily_notification_summary"][
            self.data["daily_notification_summary"]["user_id"] == user_id
        ].to_dict("records")

        # Image Path
        context["image_path"] = None

        if str(message_row["media_type"]) == "image":

            image = self.data["images"][
                self.data["images"]["image_id"] == message_row["media_id"]
            ]
            if len(image):

                context["image_path"] = image.iloc[0]["file_path"]

        # Voice Path
        context["voice_path"] = None

        if str(message_row["media_type"]) == "voice":

            voice = self.data["voice_notes"][
                self.data["voice_notes"]["voice_note_id"] == message_row["media_id"]
            ]

            if len(voice):

                context["voice_path"] = voice.iloc[0]["file_path"]


        return context