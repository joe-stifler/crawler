import networkx as nx

from .web_node import WebNode
from ..base.base_graph import BaseGraph


class WebGraph(BaseGraph):
    """Represents a directed graph of web pages for web crawling, extending the BaseGraph with web-
    specific functionalities.

    This class is designed to manage a collection of `WebNode` instances that represent individual web pages, allowing
    for the organization, traversal, and analysis of a web graph. It provides enhanced visualization methods suited for
    web graph structures.

    Methods
    -------
    __repr__()
        Provides a compact string representation of the WebGraph, including the count of nodes.
    __str__()
        Offers a detailed string representation of the web graph's nodes, listing URLs and their crawl depths.
    _repr_html_()
        Generates an HTML representation of the graph for display in Jupyter notebooks or web interfaces.

    Examples
    --------
    Creating a `WebGraph` and adding web nodes to it:

    >>> graph = WebGraph()
    >>> node1 = WebNode('https://example.com/page1')
    >>> node2 = WebNode('https://example.com/page2')
    >>> graph.add_node(node1)
    >>> graph.add_node(node2)
    >>> print(graph)
    NodeInfoSet(
        URL 0= https://example.com/page1, DEPTH = 0,
        URL 1= https://example.com/page2, DEPTH = 0
    )

    Note: The `WebNode` class and methods such as `add_node` are assumed to be defined elsewhere, with `WebNode`
    instances being compatible with the `WebGraph` structure.
    """

    def __init__(self):
        """Initializes a new WebGraph instance, ready for adding web nodes and edges."""
        super().__init__()

    def __repr__(self):
        """Returns a compact representation of the WebGraph, indicating the number of nodes.

        Returns
        -------
        str
            A string representation indicating the number of nodes in the graph.
        """
        return f"WebGraph({len(self.graph.nodes)} nodes)"

    def __str__(self):
        """Provides a detailed string representation of the web graph's nodes.

        Lists the URLs and depths of all nodes in the graph, sorted by node depth.

        Returns
        -------
        str
            A string listing the URLs and depths of all nodes in the graph.
        """
        nodes_str = ",\n".join(
            f"\tURL {index}= {node.url}, DEPTH = {node.depth}"
            for index, node in enumerate(
                sorted(self.graph.nodes, key=lambda x: x.depth)
            )
        )
        return f"NodeInfoSet(\n{nodes_str}\n)"

    def _repr_html_(self):
        """Generates an HTML representation of the web graph for display.

        This method is particularly useful for visualizing the graph structure within Jupyter notebooks or other
        environments that support HTML rendering.

        Returns
        -------
        str
            An HTML string representing the graph's nodes and their attributes.
        """
        nodes_html = "<hr>".join(
            node._repr_html_(index=index) for index, node in enumerate(self.all_nodes())
        )
        return f"<div style='border: 1px solid #eee; padding: 10px;'>{nodes_html}</div>"
