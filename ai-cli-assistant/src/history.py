history = []

def add_user_message(text):
    history.append({"role": "user", "parts": [{"text": text}]})

def add_ai_message(text):
    history.append({"role": "model", "parts": [{"text": text}]})

def get_history():
    return history

def clear_history():
    history.clear()