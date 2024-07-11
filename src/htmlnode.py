class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("not implemented yet")

    def props_to_html(self):
        if self.props is None:
            return ""

        props_html = ""

        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'

        return props_html

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, children:{self.children}, {self.props})"


"""
PRINTING SECTION TO CHECK OUTPUT
"""

# node = HTMLNode(
#     tag="div",
#     value="Hello, world!",
#     children=None,
#     props={"class": "Google", "href": "https://google.com"}
# )
# print(repr(node))
