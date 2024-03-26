import requests
import html2text
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

from ..base.base_node import BaseNode

class WebNode(BaseNode):
    """Represents a web page node in the crawl graph, with lazily fetched HTML content."""

    def __init__(self, url, **attributes):
        super().__init__(url, **attributes)
        self._soup = None
        self._content_fetched = False

    def _fetch_and_parse_html(self):
        """
        Lazily fetches the HTML content of the URL and parses it using BeautifulSoup.

        Returns:
            BeautifulSoup object: The parsed HTML content, or None if fetching fails.
        """
        try:
            response = requests.get(self.url, timeout=5)
            if response.status_code == 200:
                self._soup = BeautifulSoup(response.text, "html.parser")
            else:
                print(f"Failed to access {self.url}: {response.status_code}")
        except requests.RequestException as e:
            print(f"Failed to access {self.url}: {e}")
            self._soup = BeautifulSoup("", "html.parser")
        finally:
            self._content_fetched = True

    @property
    def soup(self):
        """
        Ensures HTML content is fetched on first access.

        Returns:
            BeautifulSoup object: The parsed HTML content.
        """
        if not self._content_fetched:
            self._fetch_and_parse_html()
        return self._soup

    def fetch_connected_hyperlinks(self):
        """
        Fetches all hyperlinks from the HTML content of the web page.
        
        Returns:
            List: The list of hyperlinks found in the HTML content.
        """
        if self.soup is None:
            return []

        urls = set()
        for link in self.soup.find_all("a"):
            href = link.get("href")
            if href and not href.startswith("#"):
                full_url = urljoin(self.url, href)
                urls.add(full_url)
        urls = list(urls)
        urls.sort()

        return urls

    def convert_to_markdown(self):
        """
        Converts the HTML content to Markdown text.

        Returns:
            str: The Markdown text representation of the HTML content.
        """
        if self.soup is None:
            return ""

        h = html2text.HTML2Text()
        h.ignore_links = True  # Optionally ignore links in the Markdown output
        return h.handle(self.soup.prettify())

    @property
    def url(self):
        return self.id
    
    @property
    def domain(self):
        """
        Extracts the domain from a URL.

        Args:
            url (str): The URL to extract the domain from.

        Returns:
            str: The extracted domain.
        """
        parsed_url = urlparse(self.url)
        return parsed_url.netloc

    def __str__(self):
        return f"WebNode(id={self.id})"

    def __repr__(self):
        return (
            f"WebNode(id={self.id})"
        )

    def _repr_html_(self, index=None):
        index_part = f"<strong>Index:</strong> {index}<br>" if index is not None else ""
        return (
            f"<div style='margin: 10px 0; padding: 5px;'>"
            f"{index_part}"
            f"<strong>Depth:</strong> {self.depth}<br>"
            f"<strong>Parent:</strong> {self.parent.id if self.parent else None}<br>"
            f"<strong>Domain:</strong> {self.domain}<br>"
            f"<strong>URL:</strong> {self.id}"
            f"</div>"
        )

    def to_markdown(self):
        """
        Converts the node's content to Markdown format.
        """
        markdown_text = self.convert_to_markdown()  # Assuming this method returns Markdown formatted text
        return markdown_text
