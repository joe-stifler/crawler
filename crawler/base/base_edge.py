from abc import ABC, abstractmethod


class BaseEdge(ABC):
    """
    Abstract base class for edges in a graph.
    """

    @abstractmethod
    def __init__(self, u, v, **attributes):
        """
        Initializes the BaseEdge.

        Args:
            u (Any): The source node.
            v (Any): The target node.
            **attributes: Additional attributes for the edge.
        """
        pass
