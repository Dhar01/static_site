import logging
from sys import argv
from copystatic import copy_files_recursive
from generate import generate_pages_recursive


def get_path():
    path = argv

    if len(path) < 2:
        return "/"

    return path[1]


def main():
    src = "static"
    dst = "docs"

    basePath = get_path()

    print("Copying static files to public directory...")
    copy_files_recursive(src, dst)

    logging.info(f"All contents are copied from {src} to {dst}")

    # # generating page
    # from_path = 'content/index.md'
    # template_path = 'template.html'
    # dest_path = 'public/index.html'

    from_path = "content"
    template_path = "template.html"
    dest_path = dst

    # generate_page(from_path, template_path, dest_path)
    generate_pages_recursive(from_path, template_path, dest_path, basePath)


if __name__ == "__main__":
    main()
