from .web_node import WebNode
from .web_graph import WebGraph
from ..base.base_crawler import BaseCrawler


class WebCrawler(BaseCrawler):
    """Represents a directed graph for web crawling."""

    def __init__(self, allowed_domains=[]):
        super().__init__()

        self.base_allowed_domains = allowed_domains
        self.session_allowed_domains = []

    def get_node(self, node_id):
        """Retrieves a node from the graph."""
        return WebNode(node_id)

    def start_new_crawling_session(self, start_node_id, restrict_to_domain=True):
        """Creates an empty subgraph."""
        start_node = self.get_node(start_node_id)

        if restrict_to_domain:
            self.session_allowed_domains = [
                start_node.domain,
            ]
        else:
            self.session_allowed_domains = []

        crawl_subgraph = WebGraph()
        crawl_subgraph.add_node(start_node)
        return crawl_subgraph

    def in_allowed_domain(self, url):
        """
        Checks if a URL is within the allowed domains.

        Args:
            url (str): The URL to check.

        Returns:
            bool: True if the URL is allowed, False otherwise.
        """
        all_allowed_domains = self.base_allowed_domains + self.session_allowed_domains

        return len(all_allowed_domains) == 0 or any(
            domain in url for domain in all_allowed_domains
        )

    def visit_node_neighborhood(self, node):
        """Fetches the web page, extracts links, and returns neighboring nodes."""
        node_neighbors = node.fetch_connected_hyperlinks()

        allowed_neighbors = [
            WebNode(neighbor)
            for neighbor in node_neighbors
            if self.in_allowed_domain(neighbor)
        ]

        return allowed_neighbors
