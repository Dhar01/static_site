import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node1, node2)

    def test_eq_false(self):
        node1 = TextNode("This is a text", "italic")
        node2 = TextNode("This is a text", "bold")
        # self.assertEqual(node1, node2)
        self.assertNotEqual(node1, node2)

    def test_all(self):
        node1 = TextNode("All will be okay", "bold", "https://bold.com")
        node2 = TextNode("All will be okay", "bold", "https://bold.com")
        self.assertEqual(node1, node2)

    def test_repr(self):
        node = TextNode("This is a text node", "text", "https://text.in")
        self.assertEqual(
            "TextNode(This is a text node, text, https://text.in)", repr(node)
        )

if __name__ == "__main__":
    unittest.main()