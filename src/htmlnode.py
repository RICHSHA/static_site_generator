class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        return_string = ''
        if self.props:
            for key, value in self.props.items():
                return_string += f' {key}="{value}"'
        return return_string

    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError('invalid HTML: no tag')
        if self.children is None:
            raise ValueError('invalid HTML: no children')
        
        return_string = f'<{self.tag}>'
        for child in self.children:
            return_string += child.to_html()
        return_string += f'</{self.tag}>'
        return return_string
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.children}, {self.props})"