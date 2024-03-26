from collections import deque
from abc import ABC, abstractmethod


class BaseCrawler(ABC):
    """Abstract base class for crawl graphs.

    This class defines the interface for crawling operations within a graph structure. It includes methods for
    retrieving nodes, starting new crawling sessions, visiting neighboring nodes, and performing a crawl using
    Breadth-First Search (BFS).

    Methods
    -------
    get_node(node_id)
        Retrieves a node from the graph.
    start_new_crawling_session(start_node_id)
        Starts a new crawling session from a given node.
    visit_node_neighborhood(node)
        Retrieves the neighborhood of a given node.
    crawl(start_node_id, max_depth=1)
        Performs the crawling process starting from a given node up to a specified depth.
    """

    def __init__(self):
        """Initializes the BaseCrawler instance."""
        super().__init__()

    @abstractmethod
    def get_node(self, node_id):
        """Retrieves a node from the graph.

        Parameters
        ----------
        node_id : str
            The identifier of the node to retrieve.

        Returns
        -------
        BaseNode
            The node object associated with the given `node_id`.
        """
        pass

    @abstractmethod
    def start_new_crawling_session(self, start_node_id):
        """Starts a new crawling session from a given node.

        Parameters
        ----------
        start_node_id : str
            The identifier of the root node to start the crawling session from.

        Returns
        -------
        BaseGraph
            A new graph object representing the crawling session.
        """
        pass

    @abstractmethod
    def visit_node_neighborhood(self, node):
        """Retrieves the neighborhood of a given node.

        Parameters
        ----------
        node : BaseNode
            The node whose neighbors should be retrieved.

        Returns
        -------
        list
            A list of neighboring nodes.
        """
        pass

    def crawl(self, start_node_id, max_depth=1):
        """Performs the crawling process using Breadth-First Search (BFS).

        Starting from a specified node, this method explores neighboring nodes up to a given depth, creating a
        subgraph of visited nodes.

        Parameters
        ----------
        start_node_id : str
            The identifier of the root node to start the crawling from.
        max_depth : int, optional
            The maximum depth to crawl. Default is 1.

        Returns
        -------
        BaseGraph
            The subgraph created during the crawling process, containing nodes and edges explored.
        """
        start_node = self.get_node(start_node_id)

        visiting_nodes = deque()
        visiting_nodes.append((start_node, 0))

        crawl_subgraph = self.start_new_crawling_session(start_node_id)

        while len(visiting_nodes) > 0:
            current_node, current_depth = visiting_nodes.popleft()
            new_depth = current_depth + 1

            if new_depth > max_depth:
                continue

            for child_node in self.visit_node_neighborhood(current_node):
                if child_node not in crawl_subgraph:
                    crawl_subgraph.add_node(child_node)
                    visiting_nodes.append((child_node, new_depth))

                crawl_subgraph.add_edge(current_node, child_node, depth=new_depth)

        return crawl_subgraph
