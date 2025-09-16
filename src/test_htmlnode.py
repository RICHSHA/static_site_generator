import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestTextNode(unittest.TestCase):
    # HTMLNode testing
    def test_props_to_html_multi_prop(self):
        node = HTMLNode(
            tag="a",
            value="Boot.dev",
            children=None,
            props={"href": "https://boot.dev", "target": "_blank"}
        )
        expected_output = ' href="https://boot.dev" target="_blank"'
        actual_output = node.props_to_html()
        self.assertEqual(actual_output, expected_output)

    def test_props_to_html_single_prop(self):
        node = HTMLNode(
            tag="a",
            value="Boot.dev",
            children=None,
            props={"href": "https://boot.dev"}
        )
        expected_output = ' href="https://boot.dev"'
        actual_output = node.props_to_html()
        self.assertEqual(actual_output, expected_output)

    def test_props_to_html_no_prop(self):
        node = HTMLNode(
            tag="a",
            value="Boot.dev",
            children=None,
            props=None
        )
        expected_output = ''
        actual_output = node.props_to_html()
        self.assertEqual(actual_output, expected_output)

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, None, {'class': 'primary'})",
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    # LeafNode testing
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    # ParentNode testing
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_children(self):
        child_node1 = LeafNode("dt", "a element")
        child_node2 = LeafNode("hr", "another element")
        child_node3 = LeafNode("ol", "dont even know")
        parent_node = ParentNode('base', [child_node1, child_node2, child_node3])
        self.assertEqual(
            parent_node.to_html(),
            '<base><dt>a element</dt><hr>another element</hr><ol>dont even know</ol></base>'
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )
if __name__ == "__main__":
    unittest.main()