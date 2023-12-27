from .source_extractor import SourceExtractor
from .credibility_checker import CredibilityChecker
from .report_generator import ReportGenerator

class SourceValidator:
    def __init__(self):
        # Initialize the components
        self.extractor = SourceExtractor()
        self.checker = CredibilityChecker()
        self.report_generator = ReportGenerator()

    def verify(self, article_content):
        # Extract sources from the article
        sources = self.extractor.extract_sources(article_content)

        # Check the credibility of each source
        scores = [self.checker.check_source(source) for source in sources]

        # Generate a report based on the sources and their scores
        report = self.report_generator.generate_report(sources, scores)

        # Calculate the overall score (you might have a different method for this)
        overall_score = sum(scores) / len(scores) if scores else 0

        return overall_score, report
