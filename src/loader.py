import pandas as pd
import os

BASE_PATH = "dataset"

def load_all_data():
    
    data = {}

    files = ["messages.csv",
        "users.csv",
        "groups.csv",
        "group_members.csv",
        "business_accounts.csv",
        "user_business_history.csv",
        "message_history.csv",
        "message_events.csv",
        "images.csv",
        "voice_notes.csv",
        "daily_notification_summary.csv"]
    for file in files:
        path = os.path.join(BASE_PATH, file)

        data[file.replace(".csv","")] = pd.read_csv(path)
    return data