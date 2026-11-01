import requests

def get_user(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 404:
        return None
    return data

