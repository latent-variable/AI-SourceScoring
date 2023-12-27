# source_info_api.py
import requests

class SourceInfoAPI:
    def __init__(self):
        self.base_url = "http://example-sourceinfo-api.com"  # Replace with actual API URL

    def get_source_info(self, source_url):
        response = requests.get(f"{self.base_url}/info", params={"url": source_url})
        if response.status_code == 200:
            return response.json()
        else:
            return None
