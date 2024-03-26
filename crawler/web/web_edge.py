from ..base.base_node import BaseEdge


class WebEdge(BaseEdge):
    """
    Represents a hyperlink (edge) between two web page nodes (u and v) in the crawl graph.

    This class extends `BaseEdge` to encapsulate attributes specific to hyperlinks found during web crawling, such as
    the relationship between pages, the anchor text, and any other relevant HTML attributes of the link.

    Parameters
    ----------
    u : WebNode
        The source node from which the hyperlink originates, representing the web page containing the hyperlink.
    v : WebNode
        The target node to which the hyperlink points, representing the destination web page of the hyperlink.
    **attributes : dict, optional
        Arbitrary keyword arguments representing additional HTML attributes of the hyperlink, such as `rel`, `title`,
        or `hreflang` attributes.

    Attributes
    ----------
    Inherits all attributes from `BaseEdge`, with the possibility of adding more through the `**attributes` parameter.

    Examples
    --------
    Assuming `node1` and `node2` are instances of `WebNode` representing different web pages, a `WebEdge` can be
    created to represent a hyperlink from `node1` to `node2` with additional attributes:

    >>> node1 = WebNode('https://example.com/page1')
    >>> node2 = WebNode('https://example.com/page2')
    >>> edge = WebEdge(node1, node2, rel='nofollow', title='Example Link')
    >>> edge.attributes['rel']
    'nofollow'
    >>> edge.attributes['title']
    'Example Link'
    """

    def __init__(self, u, v, **attributes):
        """
        Initializes a `WebEdge` instance representing a hyperlink between two web page nodes.

        Parameters
        ----------
        u : WebNode
            The source web page node.
        v : WebNode
            The target web page node.
        **attributes : dict, optional
            Additional HTML attributes of the hyperlink.
        """
        super().__init__(u, v, **attributes)
