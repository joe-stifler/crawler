import networkx as nx

from .web_node import WebNode
from ..base.base_graph import BaseGraph

class WebGraph(BaseGraph):
    def __init__(self):
        super().__init__()
        
    def __repr__(self):
        return f"NodeInfoSet({len(self.graph.nodes)} nodes)"

    def __str__(self):
        nodes_str = ",\n".join(
            f"\tURL {index}= {node.url}, DEPTH = {node.depth}"
            for index, node in enumerate(sorted(self.graph.nodes, key=lambda x: x.depth))
        )
        return f"NodeInfoSet(\n{nodes_str}\n)"
    
    def _repr_html_(self):
        nodes_html = "<hr>".join(
            node._repr_html_(index=index) for index, node in enumerate(self.all_nodes())
        )
        return f"<div style='border: 1px solid #eee; padding: 10px;'>{nodes_html}</div>"
