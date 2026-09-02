history = []


def add_user_message(message):
    history.append({
        "role": "user",
        "text": message
    })


def add_ai_message(message):
    history.append({
        "role": "model",
        "text": message
    })


def get_history():
    return history


def clear_history():
    history.clear()


def get_recent_history(limit=6):
    return history[-limit:]