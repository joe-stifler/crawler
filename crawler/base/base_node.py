from abc import ABC, abstractmethod


class BaseNode(ABC):
    """
    Abstract base class for nodes in a graph.
    """

    # @abstractmethod
    def __init__(self, node_id):
        """
        Initializes the BaseNode.

        Args:
            node_id (Any): The identifier of the node.
        """
        self._node_id = node_id
        self.depth = 0
        self.parent = None

    @property
    def id(self):
        """
        Returns the identifier of the node.

        Returns:
            Any: The identifier of the node.
        """
        return self._node_id

    @abstractmethod
    def to_markdown(self):
        """Converts the node's content to Markdown format."""
        pass

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.id == other.id
