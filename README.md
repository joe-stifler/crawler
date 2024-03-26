## Crawler: A Simple Web Crawler for Generating Markdown

Crawler is a Python package that allows you to crawl web pages and convert their content into Markdown format. This can be useful for creating documentation, notes, or other text-based representations of web content.

### Features

- **Crawls web pages:** Starting from a given URL, Crawler navigates through hyperlinks and extracts content from web pages.
- **Converts HTML to Markdown:** The extracted content is converted to Markdown format, making it easy to read and edit.
- **Supports domain restrictions:** You can specify allowed domains to limit the crawler's scope and avoid unwanted content.
- **Saves content to multiple or single files:** You can choose to save each crawled page as a separate Markdown file or combine them into a single file.
- **Visualizes the crawl graph:** Crawler provides a visualization of the crawled web pages and their connections, giving you an overview of the explored structure.

### Installation

To install Crawler, use the following command:

`pip install -e .`


### Usage

To use Crawler, follow these steps:

1. **Specify the starting URL and output folder:**
    - Run the crawler command with the starting URL and the desired output folder as arguments. For example:
    
    `crawler https://example.com output/`

2. **Optional arguments:**
    - Use the `--merge` flag to combine all crawled pages into a single Markdown file.
    - Use the `--max_depth` option to specify the maximum depth to crawl from the starting URL. The default depth is 1.

### Example

Here's an example of how to use Crawler to crawl a website and save the content to multiple Markdown files:

`crawler https://www.example.com/ output/`

This command will crawl the website starting from https://www.example.com/ and save the content of each page as a separate Markdown file in the output/ directory.

### Visualization

Crawler can also visualize the crawl graph, showing the connections between crawled pages. To do this, run the following command after crawling:

`from crawler.web.web_graph import WebGraph

# Assuming 'crawl_subgraph' is the result of the crawl
crawl_subgraph.visualize()`

This will display a visualization of the crawled web pages and their connections.

### Contributing

Contributions to Crawler are welcome! Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for more information.

### License

Crawler is licensed under the MIT License. See the LICENSE file for more information.

## AI Involvement in Content Generation

This repository utilizes artificial intelligence (AI) to assist in the content generation process.
