class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("not implemented yet")

    def props_to_html(self):
        """
        handling attributes and their value
        for example--> href="https://www.google.com"
        """
        if self.props is None:
            return ""

        props_html = ""

        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'

        return props_html

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, children:{self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, children=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        """
        representing single HTML tag with no children --> LeafNode
        """

        # if there is no value, raise ValueError
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        # if there is no tag, return raw text
        elif self.tag is None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

"""
PRINTING SECTION TO CHECK OUTPUT
"""

# node = HTMLNode(
#     tag="div",
#     value="Hello, world!",
#     children=None,
#     props={"class": "Google", "href": "https://google.com"}
# )

node = LeafNode(
    tag="a",
    value="Click me!",
    props={"href": "https://www.google.com"}
)

print(node.to_html())
