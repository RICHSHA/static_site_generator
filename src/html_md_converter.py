from markdown_block import markdown_to_blocks, block_to_block_type, BlockType
from markdown_inline import text_to_textnodes
from textnode import text_node_to_html_node
from htmlnode import ParentNode, LeafNode

# builds paragraph HTML node
def build_paragraph(block):
    lines = [line.strip() for line in block.split('\n')]
    lines = ' '.join(lines)

    text_nodes = text_to_textnodes(lines)
    html_nodes = [text_node_to_html_node(tn) for tn in text_nodes]

    return ParentNode('p', html_nodes)

def build_heading(block):
    line = block.strip()

    # counting level of heading
    level = 0
    while level<len(line) and line[level]=='#':
        level+=1
    
    # checking if ht structure is correct
    if level > 6 or line[level] != ' ' or len(line) <= level:
        raise ValueError('invalid heading block')
    
    # extract text
    text = line[level+1:].strip()

    text_nodes = text_to_textnodes(text)
    html_nodes = [text_node_to_html_node(tn) for tn in text_nodes]

    return ParentNode(f'h{level}', html_nodes)

def build_code(block): 
    pass
def build_quote(block): 
    pass
def build_ul(block): 
    pass
def build_ol(block): 
    pass

#function map for different possible md block types
BUILDERS = {
    BlockType.PARAGRAPH: build_paragraph,
    BlockType.HEADING: build_heading,
    BlockType.CODE: build_code,
    BlockType.QUOTE: build_quote,
    BlockType.ULIST: build_ul,
    BlockType.OLIST: build_ol,
}

def markdown_to_html_node(markdown):
    # initializing all wrapping parent node (div)
    parent_node = ParentNode('div', [])
    # split the markdown in blocks
    markdown_blocks = markdown_to_blocks(markdown)
    #iterate over each md block
    for block in markdown_blocks:
        #get block type
        block_type = block_to_block_type(block)
        builder = BUILDERS.get(block_type)
        if builder == None:
            raise ValueError(f'Unhandled block type: {block_type}')
        
        #build the node with builder based on block type
        node = builder(block)
        
        # add the converted node to children nodes
        parent_node.children.append(node)

    return parent_node

if __name__ == '__main__':
    test_md = """
# H1 title

## H2 with _italic_

### H3 with **bold**

#### H4 with `code`

##### H5 with a [link](https://example.com)

###### H6 end

"""

    print(markdown_to_html_node(test_md))
