from ..base.base_node import BaseEdge


class WebEdge(BaseEdge):
    """Represents a link between web pages in the crawl graph."""

    def __init__(self, u, v, **attributes):
        super().__init__(u, v, **attributes)
