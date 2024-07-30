import requests

class NotionAPI:
    def __init__(self, token):
        self.base_url = "https://api.notion.com/v1/"
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Notion-Version": "2022-06-28"
        }

    def get_content(self, database_id):
        url = f"{self.base_url}databases/{database_id}/query"
        response = requests.post(url, headers=self.headers)
        return response.json()

class ConfluenceAPI:
    def __init__(self, username, token):
        self.base_url = "https://your-domain.atlassian.net/wiki/rest/api/"
        self.auth = (username, token)

    def create_page(self, space_key, title, content):
        url = f"{self.base_url}content"
        headers = {
            "Content-Type": "application/json"
        }
        data = {
            "type": "page",
            "title": title,
            "space": {"key": space_key},
            "body": {
                "storage": {
                    "value": content,
                    "representation": "storage"
                }
            }
        }
        response = requests.post(url, auth=self.auth, headers=headers, json=data)
        return response.json()
