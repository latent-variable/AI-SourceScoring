# api_manager.py
from .fact_check_api import FactCheckAPI
from .source_info_api import SourceInfoAPI

class APIManager:
    def __init__(self):
        self.fact_check_api = FactCheckAPI()
        self.source_info_api = SourceInfoAPI()

    # You can add methods here to simplify interactions with the APIs.
