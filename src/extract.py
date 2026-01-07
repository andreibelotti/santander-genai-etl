import pandas as pd
import requests
from config.settings import BASE_URL

def extract_user_ids(path):
    df = pd.read_csv(path)
    return df["UserID"].tolist()

def extract_user_data(user_id):
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    if response.status_code == 200:
        return response.json()
    return None
