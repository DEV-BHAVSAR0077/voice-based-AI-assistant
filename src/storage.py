import json
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
FILE_PATH = os.path.join(DATA_DIR, "conversations.json")

#store conversation in json file
def store_conversation(user_text, assistant_text):
    os.makedirs(DATA_DIR, exist_ok=True)

    try:
        with open(FILE_PATH, "r") as f:
            data = json.load(f)
    except:
        data = []
    entry = {
        "user": user_text,
        "assistant": assistant_text,
        "timestamp": datetime.now().isoformat()
    }
    #append the json after every respose 
    data.append(entry)
    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)