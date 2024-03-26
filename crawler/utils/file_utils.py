import os
import re


def generate_filename_from_url(url):
    """
    Generates a safe filename from a URL.
    """
    stripped_url = re.sub(r"^https?://", "", url)
    safe_filename = re.sub(r"\W+", "_", stripped_url)
    max_length = 255
    if len(safe_filename) > max_length:
        safe_filename = safe_filename[:max_length]
    safe_filename += ".md"
    return safe_filename


def save_content_to_multiple_files(url_text_dict, directory="output"):
    """
    Saves content of each URL to its own Markdown file.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

    for url, markdown_text in url_text_dict.items():
        filename = generate_filename_from_url(url)
        header = f"# Source URL: {url}\n\n"
        content = header + markdown_text
        with open(os.path.join(directory, filename), "w", encoding="utf-8") as file:
            file.write(content)


def save_content_to_single_file(
    url_text_dict, directory="output", filename="combined_output.md"
):
    """
    Saves content of all URLs into a single Markdown file.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

    combined_content = ""
    for url, markdown_text in url_text_dict.items():
        header = f"# Source URL: {url}\n\n"
        combined_content += header + markdown_text + "\n\n---\n\n"

    with open(os.path.join(directory, filename), "w", encoding="utf-8") as file:
        file.write(combined_content)
