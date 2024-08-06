import os
import shutil
import logging
from textnode import TextNode
from genericpath import exists, isfile


def clear_directory(path: str) -> None:
    if os.path.exists("public"):
        shutil.rmtree(path)
    else:
        os.mkdir('public')

def copy_statToPub_contents(src: str, dest: str) -> None:
    if not os.path.exists(dest):
        os.mkdir(dest)

    for item in os.listdir(src):
        source = os.path.join(src, item)
        destination = os.path.join(dest, item)

        if os.path.isdir(source):
            shutil.copytree(source, destination)
            # implement logging
        else:
            shutil.copy(source, destination)
            # implement logging

    # if os.path.exists("public"):
    #     for file in os.listdir('static'):
    #         if os.path.isfile(file):
    #             shutil.copy(file, "public")
    # else:
    #     os.mkdir("public")
    #     copy_statToPub_contents()

def main():
    src = 'static'
    dst = 'public'

    # clear the destination directory
    clear_directory(dst)

    # copy contents from source to destination
    copy_statToPub_contents(src, dst)

    # node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    # print(node)

if __name__ == "__main__":
    main()