block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_ulist = "unordered_list"
block_type_olist = "ordered_list"


def markdown_to_blocks(markdown) -> list:
    """breaking into blocks"""
    blocks = []

    for block in markdown.split('\n\n'):
        if block == "":
            continue
        blocks.append(block.strip())

    return blocks

def block_to_block_type(md_block) -> str:
    """inspect markdown and determine the type of the block"""
    lines = md_block.split("\n")

    if (
        md_block.startswith("# ")
        or md_block.startswith("## ")
        or md_block.startswith("### ")
        or md_block.startswith("#### ")
        or md_block.startswith("##### ")
        or md_block.startswith("###### ")
    ):
        return block_type_heading

    elif (
        len(lines) > 1
        and lines[0].startswith("```")
        and lines[-1].startswith("```")
    ):
        return block_type_code

    elif md_block.startswith("> "):
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote

    elif md_block.startswith("* ") or md_block.startswith("- "):
        for line in lines:
            if not line.startswith("* ") or line.startswith("- "):
                return block_type_paragraph
        return block_type_ulist

    elif md_block.startswith("1. "):
        number = 1
        for line in lines:
            if not line.startswith(f"{number}. "):
                return block_type_paragraph
            number += 1
        return block_type_olist

    else:
        return block_type_paragraph