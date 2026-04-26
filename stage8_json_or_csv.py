# storage/json_store.py

import json

def save_data(data):
    with open("patients.json", "w") as f:
        json.dump(data, f)

def load_data():
    try:
        with open("patients.json", "r") as f:
            return json.load(f)
    except:
        return []
