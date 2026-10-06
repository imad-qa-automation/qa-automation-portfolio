import os
from dotenv import load_dotenv
load_dotenv()

BASE_URL = os.getenv("BASE_URL")
TOKEN = os.getenv("API_TOKEN")
MON_EMAIL = os.getenv("MON_EMAIL")

print(f"URL: {BASE_URL}")
print(f"Token: {TOKEN}")
print(f"Email: {MON_EMAIL}")