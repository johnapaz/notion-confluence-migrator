import requests
from tkinter import messagebox

def authenticate_notion(token):
    url = "https://api.notion.com/v1/users/me"
    headers = {
        "Authorization": f"Bearer {token}",
        "Notion-Version": "2022-06-28"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return True
    else:
        messagebox.showerror("Error", "Authentication failed for Notion")
        return False

def authenticate_confluence(username, token):
    url = "https://your-domain.atlassian.net/wiki/rest/api/space"
    auth = (username, token)
    response = requests.get(url, auth=auth)
    if response.status_code == 200:
        return True
    else:
        messagebox.showerror("Error", "Authentication failed for Confluence")
        return False
