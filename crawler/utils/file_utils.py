import os
import re


def generate_filename_from_url(url):
    """Generates a filesystem-safe filename from a URL.

    This function removes the protocol part of the URL, replaces non-word characters with underscores,
    and truncates the filename to a maximum length of 255 characters to ensure compatibility with most filesystems.
    A '.md' extension is appended to the resulting filename.

    Parameters
    ----------
    url : str
        The URL to be converted into a filename.

    Returns
    -------
    str
        The generated safe filename ending with '.md'.
    """
    # Protocol stripping and sanitization
    stripped_url = re.sub(r"^https?://", "", url)
    # Replace non-word characters with underscores
    safe_filename = re.sub(r"\W+", "_", stripped_url)
    # Truncate to max filesystem filename length and append extension
    max_length = 255
    if len(safe_filename) > max_length:
        safe_filename = safe_filename[:max_length]
    safe_filename += ".md"
    return safe_filename


def save_content_to_multiple_files(url_text_dict, directory="output"):
    """Saves content of each URL to its own Markdown file within the specified
    directory.

    Each URL's content is saved in a separate Markdown file named after the URL itself. The function
    ensures the creation of the target directory if it does not already exist.

    Parameters
    ----------
    url_text_dict : dict
        A dictionary where keys are URLs and values are their corresponding Markdown text content.
    directory : str, optional
        The directory path where files will be saved. Defaults to 'output'.
    """
    # Ensure target directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Write each URL's content to a separate file
    for url, markdown_text in url_text_dict.items():
        filename = generate_filename_from_url(url)
        header = f"# Source URL: {url}\n\n"
        content = header + markdown_text
        with open(os.path.join(directory, filename), "w", encoding="utf-8") as file:
            file.write(content)


def save_content_to_single_file(
    url_text_dict, directory="output", filename="combined_output.md"
):
    """Saves content of all URLs into a single Markdown file within the
    specified directory.

    Content from each URL is saved consecutively in the same file, separated by Markdown horizontal rules.
    The function ensures the creation of the target directory if it does not already exist.

    Parameters
    ----------
    url_text_dict : dict
        A dictionary where keys are URLs and values are their corresponding Markdown text content.
    directory : str, optional
        The directory path where the combined file will be saved. Defaults to 'output'.
    filename : str, optional
        The name of the file to save the combined content. Defaults to 'combined_output.md'.
    """
    # Ensure target directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Combine all content into a single string
    combined_content = ""
    for url, markdown_text in url_text_dict.items():
        header = f"# Source URL: {url}\n\n"
        combined_content += header + markdown_text + "\n\n---\n\n"

    # Write combined content to the specified file
    with open(os.path.join(directory, filename), "w", encoding="utf-8") as file:
        file.write(combined_content)
