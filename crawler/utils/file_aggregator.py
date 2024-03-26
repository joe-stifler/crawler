import glob
import os
import tempfile

# Define the path where you want to start searching for files
start_path = "."  # Use '.' for current directory or specify your own path

# Define the pattern to match .h and .cpp files
patterns = ["*.py"]

# Define the output file where the content will be aggregated
output_file = "all_headers_and_cpp_files_content_from_this_repository_in_one_file.txt"

# Define folders to ignore
ignored_folders = [
    "third_party",
    ".git",
    "scans",
    "build",
    ".vscode",
    ".github",
    "transformed_images",
]

# Get the absolute path of the start_path to ensure correct relative path
# calculation
start_path_abs = os.path.abspath(start_path)


# Function to get directory structure, excluding ignored folders
def get_directory_structure(startpath):
    structure = ""
    for root, dirs, files in os.walk(startpath, topdown=True):
        dirs[:] = [
            d
            for d in dirs
            if os.path.join(root, d)
            not in [os.path.join(startpath, f) for f in ignored_folders]
        ]  # Modify dirs in-place to ignore certain directories
        level = root.replace(startpath, "").count(os.sep)
        indent = " " * 4 * (level)
        structure += f"{indent}{os.path.basename(root)}/\n"
        subindent = " " * 4 * (level + 1)
        for f in files:
            structure += f"{subindent}{f}\n"
    return structure


# Write the aggregated content to a temporary file initially
with tempfile.NamedTemporaryFile(delete=False) as temp_outfile:
    temp_filename = temp_outfile.name
    with open(temp_filename, "w") as outfile:
        # Write directory structure first
        outfile.write("Directory Structure:\n")
        outfile.write(get_directory_structure(start_path_abs) + "\n")
        outfile.write("Aggregated File Content:\n")
        # Then write the file contents as before
        for pattern in patterns:
            for filename in glob.glob(
                os.path.join(start_path, "**", pattern), recursive=True
            ):
                if any(
                    ignored_folder in filename for ignored_folder in ignored_folders
                ):
                    continue
                relative_path = os.path.relpath(filename, start_path_abs)
                outfile.write(
                    f"/**\n * Below follows the content associated with the file:\n * {relative_path}\n */\n"
                )
                with open(filename, "r") as infile:
                    content = infile.read()
                    outfile.write(content + "\n\n")

# Now move the temporary file content to the original output file
# os.replace(temp_filename, output_file)
# mv the temporary file to the output file
os.system(f"mv {temp_filename} {output_file}")

print(
    f"All .h and .cpp files have been aggregated into {output_file}, ignoring specified folders, with directory structure prepended."
)
