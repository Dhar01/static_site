class HTMLNode:
    def __init__(self, tag, value, children, props) -> None:
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
            props_html += f" {prop}={self.props[prop]}"

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, children:{self.children}, {self.props})"