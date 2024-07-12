import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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


    def test_HTMLrepr(self):
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

    #### LeafNode ####

    def test_to_html(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>'
        )

    def test_no_tag_value(self):
        # LeafNode --> to_html()
        node = LeafNode(None, "This is a paragraph of text")
        self.assertEqual(node.to_html(), "This is a paragraph of text")

        # node = LeafNode("a", None, None, None)
        # self.assertEqual(node.to_html, ValueError("Invalid HTML: no value"))

    #### ParentNode ####

    def test_to_html_child(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>child</span></div>",
        )


    def test_to_html_manyChild(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "bold text"),
                LeafNode(None, "normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "normal text"),
            ],
        )

        self.assertEqual(
            node.to_html(),
            "<p><b>bold text</b>normal text<i>italic text</i>normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>"
        )

if __name__ == "__main__":
    unittest.main()