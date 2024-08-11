import logging

from copystatic import (
    clear_directory,
    copy_statToPub_contents
)

from generate import (
    generate_page,
    generate_pages_recursive
)

def main():
    src = 'static'
    dst = 'public'

    # clear the dest_path directory
    clear_directory(dst)

    # copy contents from src_path to dest_path
    copy_statToPub_contents(src, dst)

    logging.info(f"All contents are copied from {src} to {dst}")

    # # generating page
    # from_path = 'content/index.md'
    # template_path = 'template.html'
    # dest_path = 'public/index.html'

    from_path = 'content'
    template_path = 'template.html'
    dest_path = 'public'



    # generate_page(from_path, template_path, dest_path)
    generate_pages_recursive(from_path, template_path, dest_path)


if __name__ == "__main__":
    main()