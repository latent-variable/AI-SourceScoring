# fact_check_api.py
import requests

class FactCheckAPI:
    def __init__(self):
        self.base_url = "http://example-factcheck-api.com"  # Replace with actual API URL

    def check_fact(self, fact):
        response = requests.get(f"{self.base_url}/check", params={"fact": fact})
        if response.status_code == 200:
            return response.json()
        else:
            return None
