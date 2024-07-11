import unittest

from textnode import TextNode

class testTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node1, node2)

    def test_notEq(self):
        node1 = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node1, node2)

    def test_url(self):
        node1 = TextNode("Testing url", "text", "https://google.com")
        node2 = TextNode("Testing url", "text", "https://google.com")
        self.assertEqual(node1, node2)

    def test_noneUrl(self):
        node1 = TextNode("This is a text node", "bold", None)
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node1, node2)

    def test_repr(self):
        node = TextNode("This is a text node", "text", "https://google.com")

        self.assertEqual(
            "TextNode(This is a text node, text, https://google.com)",
            repr(node)
        )

if __name__ == "__main__":
    unittest.main()