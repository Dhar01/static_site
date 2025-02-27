import os
from block_markdown import markdown_to_html_node


def extract_title(markdown: str) -> str:
    lines = markdown.splitlines()

    for line in lines:
        if line.startswith("# "):
            return line.strip("# ")

    raise ValueError("No title found")


def generate_page(
    from_path: str, template_path: str, dest_path: str, basePath: str
) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    print(f"Processing: {from_path}")

    try:
        with open(from_path, "r") as markdown_file:
            md = markdown_file.read()

        with open(template_path, "r") as template_file:
            tmpl = template_file.read()

        # convert markdown to HTML
        html_str = markdown_to_html_node(md)
        html = html_str.to_html()

        title = extract_title(md)

        # replace {{Title}} and {{content}} placeholder5s in the template with the HTML and title
        full_html = tmpl.replace("{{ Title }}", title).replace("{{ Content }}", html)

        full_html = full_html.replace('href="/', f'href="{basePath}')
        full_html = full_html.replace('src="/', f'src="{basePath}')

        # Ensure the destination directory exists
        if not os.path.exists(os.path.dirname(dest_path)):
            os.makedirs(os.path.dirname(dest_path))

        # writing generating HTML to the destination file
        with open(dest_path, "w") as output_file:
            output_file.write(full_html)
    except ValueError as e:
        print(f"Error in file {from_path}: {e}")
        raise


def generate_pages_recursive(
    dir_path_content: str, template_path: str, dest_dir_path: str, basePath: str
) -> None:
    for filename in os.listdir(dir_path_content):
        entry_path = os.path.join(dir_path_content, filename)

        if os.path.isfile(entry_path):
            if filename.endswith(".md"):
                dest_file_path = os.path.join(
                    dest_dir_path, filename.replace(".md", ".html")
                )
                generate_page(entry_path, template_path, dest_file_path, basePath)
        else:
            next_dest_path = os.path.join(dest_dir_path, filename)
            generate_pages_recursive(
                entry_path, template_path, next_dest_path, basePath
            )
