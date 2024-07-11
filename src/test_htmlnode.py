import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {'class': 'greeting', 'href': 'https://boot.dev'},
        )

        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "working so far I guess",
        )

        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "working so far I guess")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)


    def test_repr(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )

        self.assertEqual(
            repr(node),
            "HTMLNode(div, Hello, world!, children:None, {'class': 'greeting', 'href': 'https://boot.dev'})",
        )