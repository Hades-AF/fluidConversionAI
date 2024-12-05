import os


def process_text_file(file_name: str) -> str:
    print(f"Starting File Processing for {file_name}...")
    resources_dir = os.path.join(os.path.dirname(__file__), "../resources")
    file_path = os.path.join(resources_dir, file_name)

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_name}' was not found in the 'resources' folder.")

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    print(f"Completed File Processing for {file_name}.")
    return content
