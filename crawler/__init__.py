import os
import logging
import argparse

from crawler.web.web_crawler import WebCrawler


def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(
        description="Web Crawler for generating Markdown from web pages"
    )
    parser.add_argument(
        "-u",
        "--url",
        required=True,
        type=str,
        help="The starting URL for the web crawl",
    )
    parser.add_argument(
        "-o",
        "--output_folder",
        required=True,
        type=str,
        help="The folder where Markdown files will be saved",
    )
    parser.add_argument(
        "-c",
        "--combine",
        action="store_true",
        help="Combine all pages into a single Markdown file",
    )
    parser.add_argument(
        "-md",
        "--max_depth",
        type=int,
        default=1,
        help="Maximum depth to crawl from the starting URL",
    )
    parser.add_argument(
        "-ad",
        "--allowed_domains",
        nargs="*",
        default=[],
        help="Optional list of domains the crawler is allowed to access",
    )
    parser.add_argument(
        "-v", "--verbose", type=str, default="info", help="Increase output verbosity"
    )
    # add arg to visualize or not graph
    parser.add_argument(
        "-vis",
        "--visualize",
        action="store_true",
        default=False,
        help="Enable visualization of the crawled graph",
    )

    # Parse arguments
    args = parser.parse_args()

    verbose = args.verbose or os.getenv("CRAWLER_DEBUG_VERBOSE", "info")
    verbose = verbose.upper()

    # set the verbose level
    logging.getLogger().setLevel(logging.getLevelName(verbose))

    logging.info("Starting web crawl with the following parameters:\n%s", str(args))

    # Initialize WebCrawler with the specified list of allowed domains
    # If --allowed_domains is not used, this initializes with an empty list
    crawler = WebCrawler(allowed_domains=args.allowed_domains)

    # Assuming 'crawl' is a method you will implement in WebCrawler for starting the crawling process
    # Note: You need to adjust this part as per your WebCrawler implementation details
    crawled_data = crawler.crawl(args.url, max_depth=args.max_depth)

    logging.info("Crawled graph: %s", str(crawled_data))

    if args.visualize:
        crawled_data.visualize()

    user_input = input(
        "Do you want to proceed to saving the crawled data as Markdown files? (y/N): "
    )

    if user_input.lower() == "y":
        print("Continuing...")

        # Assuming you have methods to save crawled data, which you will need to implement
        if args.combine:
            output_filename = "merged_output.md"
            crawled_data.save_to_single_file(
                directory=args.output_folder, filename=output_filename
            )
            logging.info(
                "Saved crawled data to a single Markdown file %s", output_filename
            )
        else:
            # Save to multiple Markdown files
            crawled_data.save_to_multiple_files(directory=args.output_folder)
            logging.info(
                "Saved crawled data to multiple Markdown files in %s",
                args.output_folder,
            )
    else:
        print("Stopping.")


if __name__ == "__main__":
    main()
