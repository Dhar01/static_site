import os
import shutil
from sys import argv
from copystatic import copy_files_recursive
from generate import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"
default_basepath = "/"


def get_path():
    path = argv

    if len(path) < 2:
        return default_basepath

    return path[1]


def main():
    basePath = get_path()

    # # generating page
    # from_path = 'content/index.md'
    # template_path = 'template.html'
    # dest_path = 'public/index.html'

    # from_path = "content"
    # template_path = "template.html"
    # dest_path = dst

    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public, basePath)


if __name__ == "__main__":
    main()
