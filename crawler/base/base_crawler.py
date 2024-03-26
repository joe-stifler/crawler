from collections import deque
from abc import ABC, abstractmethod

class BaseCrawler(ABC):
    """
    Abstract base class for crawl graphs that define methods for crawling operations.
    """

    def __init__(self):
        super().__init__()

    @abstractmethod
    def get_node(self, node_id):
        """
        Retrieves a node from the graph.

        Args:
            node_id (str): The identifier of the node.

        Returns:
            BaseNode: The node object.
        """
        pass
    
    @abstractmethod
    def start_new_crawling_session(self, start_node_id):
        """
        Starts a new crawling session.
        
        Args:
            start_node_id (str): The root node id to start crawling from.
            
        Returns:
            BaseGraph: The graph object.
        """
        pass

    @abstractmethod
    def visit_node_neighborhood(self, node):
        """
        Retrieves the neighborhood of a node.

        Args:
            node (BaseNode): The identifier of the node.

        Returns:
            List: The list of Node neighbors.
        """
        pass

    def crawl(self, start_node_id, max_depth=1):
        """
        Performs the crawling process using Breadth-First Search (BFS).

        Args:
            start_node_id (str): The root node id to start crawling from.
            max_depth (int, optional): The maximum depth to crawl. Defaults to 1.
        """
        start_node = self.get_node(start_node_id)

        visiting_nodes = deque()
        visiting_nodes.append((start_node, 0))

        crawl_subgraph = self.start_new_crawling_session(start_node_id)

        while len(visiting_nodes) > 0:  # Use CrawlGraph as the queue
            current_node, current_depth = visiting_nodes.popleft()
            new_depth = current_depth + 1

            if new_depth > max_depth:
                continue

            for child_node in self.visit_node_neighborhood(current_node):
                if child_node not in crawl_subgraph:
                    crawl_subgraph.add_node(child_node)
                    visiting_nodes.append((child_node, new_depth))

                crawl_subgraph.add_edge(
                    current_node, child_node, depth=new_depth
                )
        
        return crawl_subgraph
