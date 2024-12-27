history = {}


def add_to_history(user_id, text):
    if user_id not in history:
        history[user_id] = []
    history[user_id].append(text)


def get_history(user_id):
    return history.get(user_id, [])