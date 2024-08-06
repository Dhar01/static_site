import os
import shutil
import logging
from textnode import TextNode
from genericpath import exists, isfile

logging.basicConfig(level=logging.INFO, format="%(message)s")

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
            logging.info(f"Directory copied: {destination}")
        else:
            shutil.copy(source, destination)
            logging.info(f"File copied: {destination}")

def main():
    src = 'static'
    dst = 'public'

    # clear the destination directory
    clear_directory(dst)

    # copy contents from source to destination
    copy_statToPub_contents(src, dst)

    logging.info(f"All contents are copied from {src} to {dst}")

    # node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    # print(node)

if __name__ == "__main__":
    main()