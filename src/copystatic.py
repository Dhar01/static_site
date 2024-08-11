import os
import shutil
import logging

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
