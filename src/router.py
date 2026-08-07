import os
import pandas as pd


class NotificationRouter:

    def __init__(
        self,
        retriever,
        builder,
        classifier,
        evidence,
        safety,
        media
    ):

        self.retriever = retriever
        self.builder = builder
        self.classifier = classifier
        self.evidence = evidence
        self.safety = safety
        self.media = media

    def process_message(self, message):

        context = self.retriever.get_context(message)

        # -------------------------
        # IMAGE
        # -------------------------

        if str(message["media_type"]) == "image":

            image_path = os.path.join(
                "dataset",
                context["image_path"]
            )

            context["image_summary"] = self.media.process_image(
                image_path
            )

        else:

            context["image_summary"] = ""

        # -------------------------
        # AUDIO
        # -------------------------

        if str(message["media_type"]) == "voice":

            audio_path = os.path.join(
                "dataset",
                context["voice_path"]
            )

            context["voice_summary"] = self.media.process_audio(
                audio_path
            )

        else:

            context["voice_summary"] = ""

        prompt = self.builder.build_prompt(context)

        prediction = self.classifier.classify(prompt)

        prediction["evidence_message_ids"] = self.evidence.find(
            message
        )

        prediction = self.safety.apply(
            message,
            context,
            prediction
        )

        prediction["message_id"] = message["message_id"]

        return prediction