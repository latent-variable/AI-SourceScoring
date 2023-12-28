import unittest
from src.validation.source_extractor import SourceExtractor

class TestSourceExtractor(unittest.TestCase):
    def setUp(self):
        self.extractor = SourceExtractor()

    def test_extract_sources(self):
        dummy_article = "This is an article mentioning source1.com and source2.org."
        expected_sources = ["source1.com", "source2.org"]
        extracted_sources = self.extractor.extract_sources(dummy_article)
        self.assertEqual(extracted_sources, expected_sources, "Source extraction did not match expected output")

if __name__ == '__main__':
    unittest.main()
