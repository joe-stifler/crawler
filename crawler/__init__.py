import argparse

from crawler.web.web_crawler import WebCrawler


def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(
        description="Web Crawler for generating Markdown from web pages"
    )
    parser.add_argument("url", type=str, help="The starting URL for the web crawl")
    parser.add_argument(
        "output_folder", type=str, help="The folder where Markdown files will be saved"
    )
    parser.add_argument(
        "--merge",
        action="store_true",
        help="Merge all pages into a single Markdown file",
    )
    parser.add_argument(
        "--max_depth",
        type=int,
        default=1,
        help="Maximum depth to crawl from the starting URL",
    )

    # Parse arguments
    args = parser.parse_args()

    # Initialize WebCrawler with a list of allowed domains derived from the
    # input URL, if necessary
    crawler = WebCrawler(allowed_domains=[args.url])  # Adjust allowed_domains as necessary

    # Start the crawling session with the specified max_depth
    # This part assumes the WebCrawler's interface supports a max_depth
    # argument
    crawled_data = crawler.crawl(args.url, max_depth=args.max_depth)

    # Depending on the user's choice, generate and save Markdown content
    if args.merge:
        # Example function to save a single Markdown file
        # You will need to implement this logic according to your project
        # structure
        crawled_data.save_to_single_file(directory=args.output_folder, filename="merged_output.md")
    else:
        # Example function to save multiple Markdown files
        # Implementation specifics depend on your project's classes and methods
        crawled_data.save_to_multiple_files(directory=args.output_folder)


if __name__ == "__main__":
    main()
