import re

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image,
)


def extract_markdown_images(text: str) -> list:
    image_pattern = r"!\[(.*?)\]\((.*?)\)"
    return re.findall(image_pattern, text)


def extract_markdown_links(text: str) -> list:
    link_pattern = r"\[(.*?)\]\((.*?)\)"
    return re.findall(link_pattern, text)


def split_nodes_images(old_nodes: list[TextNode]) -> list[TextNode]:
    return split_contents(old_nodes, text_type_image, extract_markdown_images)


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    return split_contents(old_nodes, text_type_link, extract_markdown_links)


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: str
) -> list[TextNode]:
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue

        split_nodes = []
        sections = old_node.text.split(delimiter)

        if len(sections) % 2 == 0:
            raise ValueError("Invalid Markdown, formatted section not closed.")

        for i in range(len(sections)):
            if sections[i] == "":
                continue
            elif i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))

        new_nodes.extend(split_nodes)

    return new_nodes


def split_contents(
    old_nodes: list[TextNode], text_type: str, extraction_func
) -> list[TextNode]:
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue

        original_text = old_node.text
        elements = extraction_func(original_text)

        if len(elements) == 0:
            new_nodes.append(old_node)
            continue

        for element in elements:
            # need more work
            delimiter = ""
            if text_type == text_type_image:
                delimiter = f"![{element[0]}]({element[1]})"
            else:
                delimiter = f"[{element[0]}]({element[1]})"

            sections = original_text.split(delimiter, 1)

            if len(sections) != 2:
                raise ValueError(
                    "Invalid markdown, element section is not closed"
                )  # need to show proper messages
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))

            new_nodes.append(TextNode(element[0], text_type, element[1]))
            original_text = sections[1]

        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))

    return new_nodes


def text_to_textNodes(text: str) -> list[TextNode]:
    node = TextNode(text, text_type_text)
    text_node = split_nodes_delimiter(
        split_nodes_link(split_nodes_images([node])), "`", text_type_code
    )
    text_node = split_nodes_delimiter(text_node, "**", text_type_bold)
    text_node = split_nodes_delimiter(text_node, "*", text_type_italic)

    return text_node


def main():
    text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
    print(text_to_textNodes(text))


if __name__ == "__main__":
    main()
