from abc import ABC, abstractmethod


class BaseEdge(ABC):
    """
    Abstract base class for edges in a graph.

    This class defines a template for creating edges in a graph structure. Each edge connects two nodes and can
    contain additional attributes to represent properties of the connection.

    Parameters
    ----------
    u : Any
        The source node of the edge.
    v : Any
        The target node of the edge.
    **attributes
        Arbitrary keyword arguments representing additional attributes of the edge.

    Methods
    -------
    __init__(self, u, v, **attributes)
        Initializes a new instance of BaseEdge.
    """

    @abstractmethod
    def __init__(self, u, v, **attributes):
        """
        Initializes the BaseEdge instance with source, target, and additional attributes.

        Parameters
        ----------
        u : Any
            The source node of the edge.
        v : Any
            The target node of the edge.
        **attributes
            Arbitrary keyword arguments representing additional attributes of the edge.
        """
        pass
