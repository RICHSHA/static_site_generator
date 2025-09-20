from textnode import TextNode, TextType
import re

'''
Takes list of nodes, delimiter and text type.
Splits nodes based on delimiter and text type into multiple TextNodes.
'''
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        split = node.text.split(delimiter)
        if len(split)%2 == 0:
            raise Exception('Unclosed block')
        
        for position in range(len(split)):
            if split[position] == '':
                continue
            elif position%2 == 0:
                new_nodes.append(TextNode(split[position], TextType.TEXT))
            else:
                new_nodes.append(TextNode(split[position], text_type))
            
    return new_nodes


'''
Takes markdown text.
Matches all of the images and creates a list of tuples (alt_text, link)
'''
def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

'''
Takes markdown text.
Matches all of the links and creates a list of tuples (alt_text, link)
'''
def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

'''
Takes nodes, splits them into text and images
images -> uses extract_markdown_image() to have [(),()] of images
image[0] -> alt text 
image[1] -> url
'''
def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        temp_text = node.text
        images = extract_markdown_images(temp_text)
        if len(images) == 0:
            new_nodes.append(node)
            continue

        for image in images:
            split = temp_text.split(f'![{image[0]}]({image[1]})', maxsplit=1)
            if len(split) != 2:
                raise ValueError('invalid markdown, image section not closed')
            if split[0] != '':
                new_nodes.append(TextNode(split[0], TextType.TEXT))
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            temp_text = split[1]

        if temp_text != '':
            new_nodes.append(TextNode(temp_text, TextType.TEXT))

    return new_nodes
                

'''
Takes nodes, splits them into text and links
images -> uses extract_markdown_links() to have [(),()] of links
image[0] -> alt text 
image[1] -> url
'''
def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        temp_text = node.text
        links = extract_markdown_links(temp_text)
        if len(links) == 0:
            new_nodes.append(node)
            continue

        for link in links:
            split = temp_text.split(f'[{link[0]}]({link[1]})', maxsplit=1)
            if len(split) != 2:
                raise ValueError('invalid markdown, image section not closed')
            if split[0] != '':
                new_nodes.append(TextNode(split[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            temp_text = split[1]

        if temp_text != '':
            new_nodes.append(TextNode(temp_text, TextType.TEXT))

    return new_nodes

'''
This functions is used to split text into its TextNodes of certain MD type.
'''
def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, '`', TextType.CODE)
    nodes = split_nodes_delimiter(nodes, '_', TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, '**', TextType.BOLD)

    return nodes



if __name__ == '__main__':
    # node = TextNode("This is text with a **bolded** word", TextType.TEXT)
    # new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    # print(new_nodes)
    # split_nodes_delimiter([node], "`", TextType.CODE)

    # node = TextNode(
    #     "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
    #     TextType.TEXT,
    # )
    # new_nodes = split_nodes_image([node])
    # print(new_nodes)
    # node = TextNode(
    #     "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    #     TextType.TEXT,
    # )
    # new_nodes = split_nodes_links([node])
    # print(new_nodes)

    # print(extract_markdown_links("This is text with an [google](https://google.com)"))
    pass