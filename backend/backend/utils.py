import json

def format_message(username: str, message: str):
    return json.dumps({"user": username, "message": message})
