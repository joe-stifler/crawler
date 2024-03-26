import requests
import html2text
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

from ..base.base_node import BaseNode


class WebNode(BaseNode):
    """Represents a node in the web graph, corresponding to a web page. It supports lazily fetching
    HTML content, parsing it, extracting hyperlinks, and converting the content to Markdown.

    Parameters
    ----------
    url : str
        The URL of the web page this node represents.
    **attributes : dict, optional
        Additional attributes for the web node, passed as keyword arguments.

    Attributes
    ----------
    _soup : BeautifulSoup or None
        A BeautifulSoup object representing the parsed HTML of the page. None until the content is fetched and parsed.
    _content_fetched : bool
        Indicates whether the HTML content has been fetched and parsed.

    Methods
    -------
    _fetch_and_parse_html()
        Fetches the web page's HTML content and parses it using BeautifulSoup.
    soup
        A property that ensures the HTML content is fetched and parsed upon first access, returning a BeautifulSoup object.
    fetch_connected_hyperlinks()
        Extracts and returns all hyperlinks found within the web page's HTML content.
    convert_to_markdown()
        Converts the web page's HTML content to Markdown format.
    url
        A property returning the URL of the web page.
    domain
        Extracts and returns the domain part of the web page's URL.
    to_markdown()
        Converts the node's content (the web page's HTML) to Markdown format.

    Examples
    --------
    Creating a WebNode instance and fetching its connected hyperlinks:

    >>> node = WebNode('https://example.com')
    >>> hyperlinks = node.fetch_connected_hyperlinks()
    >>> print(hyperlinks)
    ['https://example.com/link1', 'https://example.com/link2', ...]

    Converting the node's content to Markdown:

    >>> markdown_content = node.to_markdown()
    >>> print(markdown_content[:100])  # Print the first 100 characters of the Markdown content
    """

    def __init__(self, url, **attributes):
        """Initializes a WebNode instance representing a web page.

        Parameters
        ----------
        url : str
            The URL of the web page this node represents.
        **attributes : dict, optional
            Additional attributes for the web node, such as 'depth' in the crawl graph, passed as keyword arguments.
        """
        super().__init__(url, **attributes)
        self._soup = None
        self._content_fetched = False

    def _fetch_and_parse_html(self):
        """Lazily fetches the HTML content of the node's URL and parses it using BeautifulSoup.

        This method is intended to be called internally and ensures that the web page content is fetched and parsed
        only once, when first accessed. If the fetch operation is successful, the content is stored in a BeautifulSoup
        object for further processing. If the fetch fails, it prints an error message and stores an empty BeautifulSoup
        object.

        Returns
        -------
        None
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
        """A property that ensures the HTML content is fetched and parsed upon first access. It
        returns a BeautifulSoup object containing the parsed HTML of the web page. This allows for
        lazy loading of web page content, minimizing unnecessary network operations.

        Returns
        -------
        BeautifulSoup
            The BeautifulSoup object containing the parsed HTML of the web page, or an empty BeautifulSoup object if
            the content could not be fetched.
        """
        if not self._content_fetched:
            self._fetch_and_parse_html()
        return self._soup

    def fetch_connected_hyperlinks(self):
        """Extracts and returns all hyperlinks found within the web page's HTML content. It parses
        the `a` tags to extract the `href` attribute values, resolving them to absolute URLs.

        Returns
        -------
        list of str
            A list containing the absolute URLs of all hyperlinks found within the web page's HTML content. The list
            is sorted to maintain a consistent order of URLs.
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
        """Converts the web page's HTML content to Markdown format using the html2text library. This
        method allows for a text representation of the web page's content, which can be particularly
        useful for documentation or note-taking applications.

        Returns
        -------
        str
            The Markdown text representation of the web page's HTML content. If the content has not been fetched or
            if there's no content, an empty string is returned.
        """
        if self.soup is None:
            return ""

        h = html2text.HTML2Text()
        h.ignore_links = True  # Optionally, links can be included by setting this to False
        return h.handle(self.soup.prettify())

    @property
    def url(self):
        """A property returning the URL of the web page this node represents. It provides direct
        access to the node's identifier, which in the context of a `WebNode`, is the URL.

        Returns
        -------
        str
            The URL of the web page.
        """
        return self.id

    @property
    def domain(self):
        """Extracts and returns the domain part of the web page's URL, facilitating operations that
        require domain-level granularity, such as restricting crawling activities to specific
        domains.

        Returns
        -------
        str
            The domain of the web page's URL.
        """
        parsed_url = urlparse(self.url)
        return parsed_url.netloc

    def __str__(self):
        """Provides a human-readable string representation of the WebNode, primarily for debugging
        and logging purposes.

        Returns
        -------
        str
            A string representation of the WebNode, including its URL (ID).
        """
        return f"WebNode(id={self.id})"

    def __repr__(self):
        """Provides a detailed string representation of the WebNode, suitable for interactive use in
        the interpreter.

        Returns
        -------
        str
            A detailed string representation of the WebNode, including its URL (ID).
        """
        return f"WebNode(id={self.id})"

    def _repr_html_(self, index=None):
        """Generates an HTML representation of the WebNode for display in Jupyter notebooks or web
        interfaces , incorporating additional metadata such as the node's index, depth, parent, and
        domain for enhanced visualization.

        Parameters
        ----------
        index : int, optional
            The index of the node within a collection, useful for ordering nodes in visual representations. Defaults to None.

        Returns
        -------
        str
            An HTML string representing the node's properties, including its index (if provided), depth, parent, domain, and URL.

        Example
        -------
        If rendered within a Jupyter Notebook, this method provides a rich display of the node's information, formatted as HTML.
        """
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
        """Converts the node's content, specifically the web page's HTML content, to Markdown
        format. This method leverages the `convert_to_markdown` method to produce a Markdown
        representation of the HTML content, facilitating its use in documentation, notes, or any
        other context where Markdown is preferred.

        Returns
        -------
        str
            The Markdown representation of the web page's content. If the content has not been fetched or is otherwise
            unavailable, an empty string is returned.

        Example
        -------
        >>> node = WebNode('https://example.com')
        >>> markdown_content = node.to_markdown()
        >>> print(markdown_content[:100])  # Print the first 100 characters of the Markdown content
        """
        markdown_text = (
            self.convert_to_markdown()
        )  # Assuming this method returns Markdown formatted text
        return markdown_text
