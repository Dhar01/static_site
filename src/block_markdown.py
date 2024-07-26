def markdown_to_blocks(markdown) -> list:
    blocks = []

    for block in markdown.split('\n\n'):
        if block == "":
            continue
        blocks.append(block.strip())

    return blocks
