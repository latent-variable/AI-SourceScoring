import unittest
from src.utils.data_loaders import fetch_article_content


class TestDataLoaders(unittest.TestCase):
    def test_fetch_article_content(self):
        # Example URL - replace with a suitable test URL
        test_url = "https://en.wikipedia.org/wiki/ChatGPT"
        content = fetch_article_content(test_url)
        self.assertIsNotNone(content, "Failed to fetch article content")
        self.assertIsInstance(content, str, "Article content is not a string")
        self.assertGreater(len(content), 0, "Article content is empty") 
        
        # print(content)

if __name__ == '__main__':
    unittest.main()
