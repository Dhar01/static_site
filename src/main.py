import os
import shutil
import logging
from textnode import TextNode
from genericpath import exists, isfile

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

def main():
    src = 'static'
    dst = 'public'

    # clear the dest_path directory
    clear_directory(dst)

    # copy contents from src_path to dest_path
    copy_statToPub_contents(src, dst)

    logging.info(f"All contents are copied from {src} to {dst}")

    # node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    # print(node)

if __name__ == "__main__":
    main()