from crawler import *
from pytest import fixture

# Use pytest fixtures to generate objects we know we'll reuse.
# This makes sure tests run quickly


@fixture(scope="module")
def crawler():
    import crawler

    return crawler


def test_import(crawler):
    assert crawler
