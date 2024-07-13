import unittest
from inline_markdown import (
    split_nodes_delimiter,
    split_nodes_images,
    split_nodes_link,
    extract_markdown_images,
    extract_markdown_links,
)

from textnode import(
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image
)

class TestInlineMarkdown(unittest.TestCase):
    def test_split_codeblock(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" word", text_type_text),
            ]
        )

    def test_split_boldItalic(self):
        node = TextNode("This is **bold** text with more *bolded*", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        new_nodes = split_nodes_delimiter(new_nodes, "*", text_type_italic)

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is ", text_type_text),
                TextNode("bold", text_type_bold),
                TextNode(" text with more ", text_type_text),
                TextNode("bolded", text_type_italic),
            ]
        )

    # def test_split_image(self):
    #     node = TextNode("This is ![image](image.jpg)", text_type_text)
    #     new_nodes = split_nodes_delimiter([node], "", text_type_image)
    #     self.assertEqual(
    #         new_nodes,
    #         [
    #             TextNode("This is ", text_type_text)
    #         ]
    #     )

    def test_split_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            text_type_text,
        )
        new_nodes = split_nodes_link([node])

        self.assertListEqual(
            new_nodes,
            [
                TextNode("This is text with a link ", text_type_text),
                TextNode("to boot dev", text_type_link, "https://www.boot.dev"),
                TextNode(" and ", text_type_text),
                TextNode("to youtube", text_type_link, "https://www.youtube.com/@bootdotdev"),
            ],
        )

    def test_extract_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        data = extract_markdown_images(text)
        self.assertListEqual(
            data,
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
            ]
        )

    def test_extract_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        data = extract_markdown_links(text)
        self.assertListEqual(
            data,
            [
                ("to boot dev", "https://www.boot.dev"),
                ("to youtube", "https://www.youtube.com/@bootdotdev")
            ]
        )

if __name__ == "__main__":
    unittest.main()