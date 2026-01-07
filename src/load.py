import requests
from config.settings import BASE_URL

def load_news(user, message):
    news = {
        "icon": "💰",
        "description": message
    }

    user["news"].append(news)

    response = requests.put(
        f"{BASE_URL}/users/{user['id']}",
        json=user
    )

    return response.status_code == 200
