import unittest

from block_markdown import (
    markdown_to_blocks,
    block_to_block_type,
    markdown_to_html_node,
    block_type_heading,
    block_type_paragraph,
    block_type_code,
    block_type_quote,
    block_type_olist,
    block_type_ulist,
)

class TestBlockMarkdown(unittest.TestCase):
    def test_markToBlocks(self):

        md = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""

        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                "* This is the first list item in a list block\n* This is a list item\n* This is another list item",
            ],
        )

    def test_blockToBlock(self):
        result = block_to_block_type("hello there")
        self.assertEqual(result, block_type_paragraph)

        result = block_to_block_type("> a quote\n> more quote")
        self.assertEqual(result, block_type_quote)

        result = block_to_block_type("### This is a Heading")
        self.assertEqual(result, block_type_heading)

        result = block_to_block_type("```\npython_code = input()\n```")
        self.assertEqual(result, block_type_code)

        result = block_to_block_type("* some order")
        self.assertEqual(result, block_type_ulist)

        result = block_to_block_type("1. some unorder\n2. another unorder")
        self.assertEqual(result, block_type_olist)

    def test_paragraphs(self):
        data = """
This is **bolded** paragraph.
Let's see what it can do. I don't know.
Three lines? Wow!
"""
        node = markdown_to_html_node(data)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph. Let's see what it can do. I don't know. Three lines? Wow!</p></div>",
        )

    def test_unOrderLists(self):
        data = """
- This is a list
- with items
- and *more* items
"""
        node = markdown_to_html_node(data)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul></div>",
        )

    def test_orderLists(self):
        data = """
1. This is an `ordered` list
2. with items
3. and more items
"""
        node = markdown_to_html_node(data)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_code(self):
        data = """
```
python = input()
```
"""
        node = markdown_to_html_node(data)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>python = input()\n</code></pre></div>"
        )

    def test_quote(self):
        data = """
> This is quote.
> Is it okay to see?

Change the subject. Shall we?
"""
        node = markdown_to_html_node(data)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is quote. Is it okay to see?</blockquote><p>Change the subject. Shall we?</p></div>",
        )

    def test_headings(self):
        data = """
# This is Heading

this is paragraph

### This is h3
"""
        node = markdown_to_html_node(data)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>This is Heading</h1><p>this is paragraph</p><h3>This is h3</h3></div>",
        )

if __name__ == "__main__":
    unittest.main()