from abc import ABC, abstractmethod


class BaseNode(ABC):
    """Abstract base class for nodes in a graph.

    This class provides a template for creating nodes within a graph. Each node is identified by a unique identifier
    and can have additional properties like depth and parent node for navigation or traversal purposes.

    Parameters
    ----------
    node_id : Any
        The unique identifier of the node.

    Attributes
    ----------
    depth : int
        The depth of the node within the graph. Defaults to 0.
    parent : BaseNode or None
        The parent node of this node. Useful for traversal or tree-based operations. Defaults to None.

    Methods
    -------
    to_markdown()
        Abstract method that should be implemented to convert the node's content to Markdown format.
    __hash__()
        Computes the hash based on the node's identifier.
    __eq__(other)
        Checks equality with another node based on identifiers.
    """

    def __init__(self, node_id):
        """Initializes the BaseNode instance with the provided identifier.

        Parameters
        ----------
        node_id : Any
            The unique identifier of the node.
        """
        self._node_id = node_id
        self.depth = 0
        self.parent = None

    @property
    def id(self):
        """The unique identifier of the node.

        Returns
        -------
        Any
            The identifier of the node.
        """
        return self._node_id

    @abstractmethod
    def to_markdown(self):
        """Converts the node's content to Markdown format.

        This method should be implemented by subclasses to specify how the
        node's information should be represented in Markdown.
        """
        pass

    def __hash__(self):
        """Computes the hash of the node based on its unique identifier.

        Returns
        -------
        int
            The hash of the node's identifier.
        """
        return hash(self.id)

    def __eq__(self, other):
        """Checks whether this node is equal to another node, based on their
        identifiers.

        Parameters
        ----------
        other : object
            The object to compare with.

        Returns
        -------
        bool
            True if `other` is an instance of the same class and their identifiers match, otherwise False.
        """
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.id == other.id
