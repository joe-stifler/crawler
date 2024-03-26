import networkx as nx
import matplotlib.pyplot as plt

# Assuming save_content_to_multiple_files and save_content_to_single_file
# are defined elsewhere
from ..utils.file_utils import (
    save_content_to_multiple_files,
    save_content_to_single_file,
)


class BaseGraph:
    """A base class for managing and visualizing graphs using NetworkX and matplotlib.

    This class encapsulates a directed graph and provides methods for node and edge manipulation,
    visualization, and exporting the graph data.

    Attributes
    ----------
    graph : nx.DiGraph
        A directed graph instance from NetworkX where nodes and edges can be added or manipulated.

    Methods
    -------
    add_node(node)
        Adds a node to the graph.
    add_edge(u, v, **attributes)
        Adds an edge between two nodes in the graph, with optional attributes.
    get_node(node_id)
        Retrieves a node from the graph by its identifier.
    all_nodes()
        Returns a list of all nodes in the graph.
    visualize()
        Visualizes the graph using matplotlib.
    to_markdown()
        Converts all graph nodes to a markdown text dictionary.
    save_to_multiple_files(directory="output")
        Saves the graph nodes' markdown representations to multiple files in the specified directory.
    save_to_single_file(directory="output", filename="combined_output.md")
        Combines the markdown representations of all graph nodes and saves them to a single file.
    """

    def __init__(self):
        """Initializes a new instance of BaseGraph."""
        self.graph = nx.DiGraph()

    def add_node(self, node):
        """Adds a node to the graph.

        Parameters
        ----------
        node : BaseNode
            The node to be added to the graph. The node must have a unique identifier.
        """
        self.graph.add_node(node.id, node=node)

    def add_edge(self, u, v, **attributes):
        """Adds an edge between two nodes in the graph, with optional attributes.

        Parameters
        ----------
        u : BaseNode
            The source node of the edge.
        v : BaseNode
            The target node of the edge.
        **attributes
            Arbitrary keyword arguments representing additional attributes of the edge.
        """
        if u.id == v.id:
            return
        self.graph.add_edge(u.id, v.id, **attributes)

    def get_node(self, node_id):
        """Retrieves a node from the graph by its identifier.

        Parameters
        ----------
        node_id : Any
            The unique identifier of the node to retrieve.

        Returns
        -------
        BaseNode
            The node associated with the given identifier.
        """
        return self.graph.nodes[node_id]["node"]

    def all_nodes(self):
        """Returns a list of all nodes in the graph.

        Returns
        -------
        list of BaseNode
            A list containing all nodes in the graph.
        """
        return [node["node"] for node in self.graph.nodes.values()]

    def __contains__(self, node):
        """Checks if a node is in the graph.

        Parameters
        ----------
        node : BaseNode
            The node to check for in the graph.

        Returns
        -------
        bool
            True if the node is in the graph, False otherwise.
        """
        return node.id in self.graph.nodes

    def visualize(self):
        """Visualizes the graph using matplotlib.

        This method generates a visual representation of the graph, displaying nodes, edges, and
        optionally labels.
        """
        # Prepare node labels based on WebNode IDs
        node_labels = {node.id: f"{idx}" for idx, node in enumerate(self.all_nodes())}

        # Set up the figure layout
        fig, ax = plt.subplots(figsize=(15, 8))
        plt.subplots_adjust(left=0.1, right=0.75)
        ax_graph = plt.subplot(121)

        # Draw the graph
        pos = nx.spring_layout(self.graph)  # positions for all nodes
        nx.draw(
            self.graph,
            pos,
            with_labels=True,
            labels=node_labels,
            node_size=50,
            font_size=8,
            ax=ax_graph,
        )

        # Prepare and show the URL mapping on the right
        textstr = "\n".join([f"{idx}: {node.id}" for idx, node in enumerate(self.all_nodes())])
        props = dict(boxstyle="round", facecolor="wheat", alpha=0.5)

        # Add a side subplot for URL mapping
        ax_mapping = plt.subplot(122)
        plt.axis("off")
        ax_mapping.text(
            0.05,
            0.95,
            textstr,
            transform=ax_mapping.transAxes,
            fontsize=8,
            verticalalignment="top",
            bbox=props,
        )

        plt.show()

    def to_markdown(self):
        """Converts all graph nodes to a markdown text dictionary.

        Returns
        -------
        dict
            A dictionary where keys are URLs (assuming each node has a URL attribute) and values are the markdown
            representation of nodes.
        """
        url_text_dict = {}
        for node in self.all_nodes():
            url_text_dict[node.url] = (
                node.to_markdown()
            )  # Assuming each node has a 'to_markdown' method
        return url_text_dict

    def save_to_multiple_files(self, directory="output"):
        """Saves the graph nodes' markdown representations to multiple files in the specified
        directory.

        Parameters
        ----------
        directory : str, optional
            The directory where the files will be saved. Default is "output".
        """
        url_text_dict = self.to_markdown()
        save_content_to_multiple_files(url_text_dict, directory)

    def save_to_single_file(self, directory="output", filename="combined_output.md"):
        """Combines the markdown representations of all graph nodes and saves them to a single file.

        Parameters
        ----------
        directory : str, optional
            The directory where the output file will be saved. Default is "output".
        filename : str, optional
            The name of the output file. Default is "combined_output.md".
        """
        url_text_dict = self.to_markdown()
        save_content_to_single_file(url_text_dict, directory, filename)
