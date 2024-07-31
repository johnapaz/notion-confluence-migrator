import requests
from dotenv import load_dotenv
import os

load_dotenv()

NOTION_API_KEY = os.getenv("NOTION_API_KEY")
CONFLUENCE_API_KEY = os.getenv("CONFLUENCE_API_KEY")

def get_sites():
    # Implement the logic to fetch sites
    response = requests.get("YOUR_API_ENDPOINT_FOR_SITES", headers={"Authorization": f"Bearer {CONFLUENCE_API_KEY}"})
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def get_spaces(site):
    # Implement the logic to fetch spaces for a given site
    response = requests.get(f"YOUR_API_ENDPOINT_FOR_SPACES/{site}", headers={"Authorization": f"Bearer {CONFLUENCE_API_KEY}"})
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def create_space(site, space_name, space_key):
    # Implement the logic to create a space
    data = {"name": space_name, "key": space_key}
    response = requests.post(f"YOUR_API_ENDPOINT_FOR_SPACES/{site}", json=data, headers={"Authorization": f"Bearer {CONFLUENCE_API_KEY}"})
    if response.status_code == 201:
        return response.json()
    else:
        response.raise_for_status()
