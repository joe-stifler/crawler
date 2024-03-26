from crawler.utils.file_utils import (
    generate_filename_from_url,
    save_content_to_single_file,
)


def test_generate_filename_from_url():
    url = "https://example.com/page?query=123"
    filename = generate_filename_from_url(url)
    assert filename == "example_com_page_query_123.md"


def test_save_content_to_single_file(tmp_path):
    url_text_dict = {"https://example.com": "# Example Content"}
    save_content_to_single_file(url_text_dict, directory=tmp_path, filename="test.md")
    saved_file = tmp_path / "test.md"
    assert saved_file.exists()
