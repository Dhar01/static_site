import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image,
    text_node_to_html_node,
)

class testTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertEqual(node1, node2)

    def test_notEq(self):
        node1 = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is a text node", text_type_italic)
        self.assertNotEqual(node1, node2)

    def test_url(self):
        node1 = TextNode("Testing url", text_type_text, "https://google.com")
        node2 = TextNode("Testing url", text_type_text, "https://google.com")
        self.assertEqual(node1, node2)

    def test_noneUrl(self):
        node1 = TextNode("This is a text node", text_type_bold, None)
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertEqual(node1, node2)

    def test_repr(self):
        node = TextNode("This is a text node", text_type_bold, "https://google.com")

        self.assertEqual(
            "TextNode(This is a text node, bold, https://google.com)",
            repr(node)
        )

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", text_type_text)
        html_node = text_node_to_html_node(node)

        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("A image", text_type_image, "https://boot.dev")
        html_node = text_node_to_html_node(node)

        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://boot.dev", "alt": "A image"},
        )

if __name__ == "__main__":
    unittest.main()