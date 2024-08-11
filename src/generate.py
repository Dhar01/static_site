import os
import shutil
import logging
from genericpath import exists, isfile
from block_markdown import markdown_to_html_node

# logging
logging.basicConfig(level=logging.INFO, format="%(message)s")

def clear_directory(path: str) -> None:
    if os.path.exists(path):
        shutil.rmtree(path)
        logging.info(f"Directory '{path}' cleaned!")
    else:
        os.mkdir(path)
        logging.info(f"Directory '{path}' created!")

def copy_statToPub_contents(src: str, dest: str) -> None:
    if not os.path.exists(dest):
        os.mkdir(dest)

    for filename in os.listdir(src):
        src_path = os.path.join(src, filename)
        dest_path = os.path.join(dest, filename)

        if os.path.isdir(src_path):
            shutil.copytree(src_path, dest_path)
            logging.info(f"Directory copied: {dest_path}")
        else:
            shutil.copy(src_path, dest_path)
            logging.info(f"File copied: {dest_path}")

def extract_title(markdown: str) -> str:
    lines = markdown.splitlines()

    for line in lines:
        if line.startswith('# '):
            return line.strip('# ')

    raise ValueError("No title found")

def generate_page(from_path: str, template_path: str, dest_path: str) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, 'r') as markdown_file:
        md = markdown_file.read()

    with open(template_path, 'r') as template_file:
        tmpl = template_file.read()

    # convert markdown to HTML
    html_str = markdown_to_html_node(md)
    html = html_str.to_html()

    title = extract_title(md)

    # replace {{Title}} and {{content}} placeholder5s in the template with the HTML and title
    full_html = tmpl.replace('{{ Title }}', title).replace('{{ Content }}', html)

    # Ensure the destination directory exists
    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))

    # writing generating HTML to the destination file
    with open(dest_path, 'w') as output_file:
        output_file.write(full_html)


def main():
    pass

if __name__ == '__main__':
    main()