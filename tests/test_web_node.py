import pytest
from crawler.web.web_node import WebNode


def test_web_node_initialization():
    url = "https://example.com"
    node = WebNode(url)
    assert node.url == url
    assert node.depth == 0
    assert node.parent is None


def test_web_node_domain_extraction():
    node = WebNode("https://example.com/page")
    assert node.domain == "example.com"
