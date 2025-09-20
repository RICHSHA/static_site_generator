from enum import Enum

class BlockType(Enum):
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    ULIST = 'unordered_list'
    OLIST = 'ordered_list'

'''
This functions splits markdown text into blocks by splitting it via newline.
'''
def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    filtered_blocks = []

    for block in blocks:
        block = block.strip()
        if block == '':
            continue
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(block):
    lines = block.split('\n')

    if block.startswith(('# ', '## ', '### ', '#### ', '##### ', '###### ')):
        return BlockType.HEADING
    elif len(lines) > 1 and lines[0].startswith('```') and lines[-1].startswith('```'):
        return BlockType.CODE
    elif block.startswith('>'):
        for line in lines:
            if not line.startswith('>'):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    elif block.startswith('- '):
        for line in lines:
            if not line.startswith('- '):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    elif block.startswith('1. '):
        i = 1
        for line in lines:
            if not line.startswith(f'{i}. '):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.OLIST
    return BlockType.PARAGRAPH

if __name__ == '__main__':
    pass