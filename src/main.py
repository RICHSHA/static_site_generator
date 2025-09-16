from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode

# new_node = TextNode('This is some anchor text', TextType.LINK, 'https://www.boot.dev')
# print(new_node)

# node1 = HTMLNode(
#     tag="a",
#     value="Boot.dev",
#     children=None,
#     props={"href": "https://boot.dev", "target": "_blank"}
# )

# node2 = HTMLNode(
#     tag="img",
#     value=None, # Image tags usually don't have a value directly
#     children=None,
#     props={"src": "image.png", "alt": "A mystical forest"}
# )

# node3 = HTMLNode(
#     tag="p",
#     value="Some text for the paragraph",
#     children=None,
#     props={"class": "important-message"}
# )

# print(node1)
# print(node2)
# print(node3)


child_node = LeafNode("span", "child")
parent_node = ParentNode("div", [child_node])

print(child_node)
print(parent_node)
print(parent_node.to_html())