import os
import networkx as nx
import matplotlib.pyplot as plt

from ..utils.file_utils import (
    save_content_to_multiple_files,
    save_content_to_single_file,
)


class BaseGraph:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_node(self, node):
        self.graph.add_node(node.id, node=node)

    def add_edge(self, u, v, **attributes):
        if u.id == v.id:
            return
        self.graph.add_edge(u.id, v.id, **attributes)

    def get_node(self, node_id):
        return self.graph.nodes[node_id]["node"]

    def all_nodes(self):
        # return self.graph.nodes.values()
        return [node["node"] for node in self.graph.nodes.values()]

    def __contains__(self, node):
        return node.id in self.graph.nodes

    def visualize(self):
        """
        Visualizes the graph using matplotlib.
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
        textstr = "\n".join(
            [f"{idx}: {node.id}" for idx, node in enumerate(self.all_nodes())]
        )
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
        """Converts all graph nodes to a markdown text dictionary."""
        url_text_dict = {}
        for node in self.all_nodes():
            url_text_dict[
                node.url
            ] = node.to_markdown()  # Assuming each node has a 'to_markdown' method
        return url_text_dict

    def save_to_multiple_files(self, directory="output"):
        url_text_dict = self.to_markdown()
        save_content_to_multiple_files(url_text_dict, directory)

    def save_to_single_file(self, directory="output", filename="combined_output.md"):
        url_text_dict = self.to_markdown()
        save_content_to_single_file(url_text_dict, directory, filename)
