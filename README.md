**Crawler: A Simple Web Crawler to Convert HTML Content into Markdown**

Crawler is a Python package designed to crawl web pages and convert their content into Markdown format. This tool is ideal for creating documentation, notes, or other text-based representations of web content.

### Motivation

While there are existing Python libraries for web crawling and Markdown conversion, this project was born out of a desire to:

1. **Learn and Experiment:** This project was an opportunity to learn new technologies and explore different approaches to crawling and content conversion.
2. **Sharpen Python Skills:** It provided a chance to practice and improve Python programming skills, with a focus on object-oriented design and design patterns.
3. **Facilitate LLM Interactions:** With the rise of large language models (LLMs), the need to gather information from various sources (internet, file systems, databases) became apparent. This tool was created to streamline the process of extracting and combining content into a format suitable for LLM context.
4. **Future Expansion:** The project's roadmap includes expanding functionality to handle not only URLs but also local file paths and even GitHub repositories, enabling the extraction and combination of code files for LLM context.

### **Features**

- **Crawls web pages:** Starts from a given URL and navigates through hyperlinks to extract content.
- **Converts HTML to Markdown:** Transforms extracted web content into Markdown for ease of reading and editing.
- **Domain restrictions:** Limits crawling scope to specified domains to avoid crawling unwanted content.
- **Flexible output options:** Content can be saved as individual Markdown files or combined into a single file.
- **Graph visualization:** Offers a visual representation of the crawl, illustrating the structure explored.

### **Installation**

Install Crawler with pip:

```
pip install -e .

```

### **Usage**

Crawler is command-line friendly. Here's how to get started:

1. **Launch a crawl:**
Use the command **`crawler`** followed by the required flags and options. For instance:
    
    ```
    crawler -u https://example.com -o output/
    ```
    
2. **Command-line arguments:**
    - **`u, --url`**: (Required) The starting URL for the crawl.
    - **`o, --output_folder`**: (Required) Destination folder for Markdown files.
    - **`c, --combine`**: Combine all crawled pages into a single Markdown file.
    - **`md, --max_depth`**: Set the maximum crawl depth (default is 1).
    - **`ad, --allowed_domains`**: Specify domains the crawler can access.
    - **`v, --verbose`**: Set verbosity level (**`info`** by default).
    - **`vis, --visualize`**: Enable post-crawl visualization of the graph.

### **Example**

Crawl a website and save each page as a Markdown file in the specified **`output/`** folder:

```
crawler -u https://www.example.com -o output/
```

### **Visualization**

To visualize the crawl graph:

```python
from crawler.web.web_graph import WebGraph

web_crawler = WebCrawler(allowed_domains=["example.com"])
crawl_subgraph = web_crawler.crawl(
    "https://www.example.com", max_depth=1
)
crawl_subgraph.visualize()
```

This displays the structure of the crawled web pages and their links.

### **Roadmap**

### Crawling Enhancements:

- **Parallel crawling for efficiency:** Implement parallel crawling techniques to significantly speed up the crawling process, especially for large websites or complex directory structures.
- **File system crawling:** Extend crawling capabilities beyond web pages to include local file systems, allowing users to extract content from files within specified directories.
- **GitHub repository crawling:** Enable the crawling of GitHub repositories to extract code from specific file types (e.g., .py, .cpp, .h) and combine them for use as context in large language models (LLMs).
- **Support crawling for specific file patterns:** Allow users to define specific file patterns or extensions to target during the crawl, providing more granular control over the content extraction process.

### Caching and Storage:

- **Caching with expiration:** Implement a caching mechanism to store crawled web pages or files locally, reducing redundant requests and improving performance for repeated crawls. Set expiration times for cached content to ensure freshness.
- **Database support for cache:** Explore storing cached content in a database for more efficient retrieval and management, potentially enabling access to cached pages outside the Crawler program itself.

### Output and Customization:

- **Support for additional output formats:** Expand output options beyond Markdown to include other formats such as HTML, PDF, or plain text, providing flexibility for different use cases.
- **Custom parsing rules:** Allow users to define custom parsing rules to handle websites with unique structures or content formats, ensuring accurate and tailored content extraction.

### Visualization:

- **Enhanced graph visualization:** Improve the visualization of the crawl graph with more interactive features, such as filtering, zooming, and highlighting specific nodes or connections, to provide a clearer and more insightful overview of the crawled structure.

### **Contributing**

Your contributions are welcome! Please refer to [CONTRIBUTING.md](https://chat.openai.com/c/CONTRIBUTING.md) for guidelines.

### **License**

Crawler is released under the MIT License. See the [LICENSE](https://chat.openai.com/c/LICENSE) file for more details.

### **AI Involvement in Content Generation**

This project leverages AI to assist in generating content.
