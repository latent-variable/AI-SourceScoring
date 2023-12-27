import argparse
import logging
from validation.source_validator import SourceValidator
from utils.data_loaders import fetch_article_content

def setup_logging():
    """Set up logging for the application."""
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description='SourceScore: AI-powered Source Verification Tool')
    parser.add_argument('article_path', type=str, help='Path to the article file for source checking')
    return parser.parse_args()

def main():
    """Main function of the SourceScore application."""
    setup_logging()
    args = parse_arguments()

    logging.info(f"Starting source verification for: {args.article_path}")

    # Initialize the source validator
    source_validator = SourceValidator()

    # Load and process the article
    # Placeholder for loading and processing the article
    article_content = fetch_article_content(args.article_path)  

    # Perform source verification
    score, report = source_validator.verify(article_content)
    
    logging.info(f"Verification Complete. SourceScore: {score}")
    logging.info(f"Verification Report: \n{report}")

if __name__ == "__main__":
    main()
