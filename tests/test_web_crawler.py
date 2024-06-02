from crawler.web.web_crawler import WebCrawler
from crawler.web.web_node import WebNode
from crawler.web.web_graph import WebGraph
from bs4 import BeautifulSoup

from pytest import fixture


# Fixtures for reusable objects
@fixture(scope="module")
def crawler():
    return WebCrawler(
        allowed_domains=["example.com"]
    )  # Adjust allowed_domains as needed


@fixture
def web_node():
    return WebNode("https://example.com/page1")


# Test basic imports and object creation
def test_import(crawler):
    assert crawler


def test_web_node_creation(web_node):
    assert web_node.url == "https://example.com/page1"


def test_crawler_initialization():
    crawler = WebCrawler(allowed_domains=["example.com"])
    assert "example.com" in crawler.base_allowed_domains


# Test WebCrawler methods
def test_get_node(crawler):
    node = crawler.get_node("https://example.com/page2")
    assert isinstance(node, WebNode)
    assert node.url == "https://example.com/page2"


def test_start_new_crawling_session(crawler):
    graph = crawler.start_new_crawling_session("https://example.com/start")
    assert isinstance(graph, WebGraph)
    assert len(graph.all_nodes()) == 1


def test_in_allowed_domain(crawler):
    assert crawler.in_allowed_domain("https://example.com/allowed")
    assert not crawler.in_allowed_domain("https://otherdomain.com/not_allowed")


def test_visit_node_neighborhood(crawler, web_node):
    # Mock or provide actual HTML content for testing
    web_node.cache[web_node.url] = BeautifulSoup(
        """<a href="/link1">Link 1</a> <a href="https://otherdomain.com/link2">Link 2</a>""",
        "html.parser",
    )
    neighbors = crawler.visit_node_neighborhood(web_node)
    assert len(neighbors) == 1  # Only the allowed link should be included
    assert neighbors[0].url == "https://example.com/link1"


# Test WebNode methods
def test_web_node_soup(web_node):
    # Mock or provide actual HTML content for testing
    web_node.cache[web_node.url] = BeautifulSoup("<h1>Example Page</h1>", "html.parser")
    assert web_node.soup.find("h1").text == "Example Page"


def test_fetch_connected_hyperlinks(web_node):
    # Mock or provide actual HTML content for testing
    web_node.cache[web_node.url] = BeautifulSoup(
        """<a href="/link1">Link 1</a> <a href="/link2">Link 2</a>""",
        "html.parser",
    )
    links = web_node.fetch_connected_hyperlinks()
    assert links == ["https://example.com/link1", "https://example.com/link2"]


def test_convert_to_markdown(web_node):
    # Mock or provide actual HTML content for testing
    web_node.cache[web_node.url] = BeautifulSoup("<h1>Example Page</h1>", "html.parser")
    markdown = web_node.convert_to_markdown()
    assert markdown.startswith("#  Example Page")


# Test WebGraph methods
def test_web_graph_add_node(crawler):
    graph = crawler.start_new_crawling_session("https://example.com/start")
    node = crawler.get_node("https://example.com/page1")
    graph.add_node(node)
    assert len(graph.all_nodes()) == 2


def test_web_graph_add_edge(crawler):
    graph = crawler.start_new_crawling_session("https://example.com/start")
    node1 = crawler.get_node("https://example.com/page1")
    node2 = crawler.get_node("https://example.com/page2")
    graph.add_edge(node1, node2)
    assert graph.graph.has_edge(node1.id, node2.id)
