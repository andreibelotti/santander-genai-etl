import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://sdw-2023-prd.up.railway.app"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
