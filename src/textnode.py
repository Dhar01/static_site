class TextNode:
    """
    text = text content of the node
    text_type = type of text, a string like bold or italic
    url = url, default to None if nothing passed in
    """
    def __init__(self, text, text_type, url=None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other) -> bool:
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

        # if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
        #     return True

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"