import re

from textnode import(
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image,
)

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter, text_type: str) -> list[TextNode]:
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue

        split_nodes = []
        sections = old_node.text.split(delimiter)

        if len(sections) % 2 == 0:
            raise ValueError("Invalid Markdown Syntax")

        for i in range(len(sections)):
            if sections[i] == "":
                continue
            elif i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))

        new_nodes.extend(split_nodes)

    return new_nodes

def extract_markdown_images(text: str) -> tuple:
    image_pattern = r"!\[(.*?)\]\((.*?)\)"
    return re.findall(image_pattern, text)

def extract_markdown_links(text: str) -> tuple:
    link_pattern = r"\[(.*?)\]\((.*?)\)"
    return re.findall(link_pattern, text)

def split_nodes_images(old_nodes: list[TextNode]) -> list[TextNode]:
    pass

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue

        original_text = old_node.text
        links = extract_markdown_links(original_text)

        if len(links) == 0:
            new_nodes.append(old_node)
            continue

        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))

            new_nodes.append(TextNode(link[0], text_type_link, link[1]))
            original_text = sections[1]

        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))

    return new_nodes

# REQUIREMENTS

# node = TextNode("This is text with a `code block` word", text_type_text)
# new_nodes = split_nodes_delimiter([node], "`", text_type_code)

# #output
# [
#     TextNode("This is text with a ", text_type_text),
#     TextNode("code block", text_type_code),
#     TextNode(" word", text_type_text),
# ]
# print(new_nodes)