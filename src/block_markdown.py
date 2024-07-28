from htmlnode import ParentNode
from textnode import text_node_to_html_node
from inline_markdown import text_to_textNodes

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_ulist = "unordered_list"
block_type_olist = "ordered_list"

def markdown_to_blocks(markdown: str) -> list:
    """breaking into blocks"""
    blocks = []

    for block in markdown.split('\n\n'):
        if block == "":
            continue
        blocks.append(block.strip())

    return blocks

def block_to_block_type(md_block: str) -> str:
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

def markdown_to_html_node(markdown) -> ParentNode:
    """Convert a full Markdown into a single HTMLNode"""
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        node = block_to_HTMLNode(block)
        children.append(node)

    return ParentNode("div", children, None)

def block_to_HTMLNode(block: str) -> ParentNode:
    block_type = block_to_block_type(block)

    if block_type == block_type_paragraph:
        return paragraph_to_htmlNode(block)
    elif block_type == block_type_heading:
        return heading_to_htmlNode(block)
    elif block_type == block_type_code:
        return code_to_htmlNode(block)
    elif block_type == block_type_quote:
        return quote_to_htmlNode(block)
    elif block_type == block_type_ulist:
        return ulist_to_htmlNode(block)
    elif block_type == block_type_olist:
        return olist_to_htmlNode(block)
    else:
        raise ValueError("Invalid Block Type")

def text_to_children(text: str) -> list[ParentNode]:
    children = []

    textNodes = text_to_textNodes(text)
    for textNode in textNodes:
        htmlNode = text_node_to_html_node(textNode)
        children.append(htmlNode)

    return children

def paragraph_to_htmlNode(block: str) -> ParentNode:
    lines = block.split('\n')
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def heading_to_htmlNode(block: str) -> ParentNode:
    pass
    # return ParentNode("h", value)

def code_to_htmlNode(block: str) -> ParentNode:
    pass
    # return ParentNode("code", value)

def quote_to_htmlNode(block: str) -> ParentNode:
    # more code
    children = text_to_children(quotes)
    return ParentNode("blockquote", children)

def ulist_to_htmlNode(block: str) -> ParentNode:
    # more code
    children = text_to_children(unordered_list)
    return ParentNode("ul", children)

def olist_to_htmlNode(block: str) -> ParentNode:
    # more code
    children = text_to_children(ordered_list)
    return ParentNode("ol", children)