import pytest
from crawler.web.web_node import WebNode
from crawler.web.web_graph import WebGraph


def test_add_node_to_web_graph():
    graph = WebGraph()
    node = WebNode("https://example.com")
    graph.add_node(node)
    assert node in graph


def test_add_edge_to_web_graph():
    graph = WebGraph()
    node1 = WebNode("https://example.com/page1")
    node2 = WebNode("https://example.com/page2")
    graph.add_node(node1)
    graph.add_node(node2)
    graph.add_edge(node1, node2)
    assert graph.graph.has_edge(node1.id, node2.id)
