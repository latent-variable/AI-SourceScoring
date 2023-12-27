# data_loaders.py
import requests
from bs4 import BeautifulSoup


def fetch_article_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        # Use BeautifulSoup for HTML parsing
        soup = BeautifulSoup(response.content, 'html.parser')
        article_content = soup.get_text()  # Modify this based on the structure of the webpage
        return article_content
    except requests.RequestException as e:
        print(f"Error fetching article: {e}")
        return None


def load_data_file(file_path):
    # Load data from a file
    # Placeholder for data loading logic
    try:
        with open(file_path, 'r') as file:
            data = file.read()
        return data
    except IOError as e:
        print(f"Error reading file {file_path}: {e}")
        return None
