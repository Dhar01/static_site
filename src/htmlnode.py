class HTMLNode:
    """Representing a node in an HTML document tree and rendering"""
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> Exception:
        raise NotImplementedError("to_html method not implemented yet")

    def props_to_html(self) -> str:
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
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    """Representing single HTML tag with no children --> LeafNode"""
    def __init__(self, tag, value, props=None) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
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


class ParentNode(HTMLNode):
    """Handling the nesting of HTML nodes inside of one another --> ParentNode"""
    def __init__(self, tag, children, props=None) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("Invalid HTML: no tags")
        if self.children is None:
            raise ValueError("Invalid HTML: no children")

        child_html = ""

        for child in self.children:
            child_html += child.to_html()

        return f"<{self.tag}{self.props_to_html()}>{child_html}</{self.tag}>"

    def __repr__(self) -> str:
        return f"ParentNode({self.tag}, Children: {self.children}, {self.props})"

def main():
    pass

if __name__ == "__main__":
    main()