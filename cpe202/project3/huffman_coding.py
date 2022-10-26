"""Project 3: Huffman Coding.
Course: CPE202
Quarter: Spring 2020
Author: Henry Berman
"""
from min_pq import *
from huffman import *
from huffman_bit_reader import *
from huffman_bit_writer import *

def cnt_freq(filename):
    """counts frequency of characters in a file
    Args:
        filename (str): the filename
    Returns:
        (list): list of size 256 containing frequencies of all chars
    """
    file = open(filename, "r")
    counts = [0] * 256
    for line in file:
        for char in line:
            counts[ord(char)] += 1
    counts[0] = 1
    file.close()
    return counts


def create_huff_tree(list_of_freqs):
    """creates huffman tree from a list of character frequencies.
    Args:
        list_of_freqs (list): list of character frequencies
    Returns:
        (None or HuffmanNode): returns huffman tree
    """
    huff_nodes = []
    if list_of_freqs == [0] * 256:
        return None
    for i, val in enumerate(list_of_freqs):
        if val != 0:
            huff_nodes.append(HuffmanNode(val, chr(i)))
    min_pq = MinPQ(huff_nodes)
    while min_pq.size() > 1:
        huff1 = min_pq.del_min()
        huff2 = min_pq.del_min()
        new_node = HuffmanNode(huff1.freq + huff2.freq, None, huff1, huff2)
        if huff1.char < huff2.char:
            new_node.char = huff1.char
        else:
            new_node.char = huff2.char
        min_pq.insert(new_node)
    return min_pq.min()



def create_huff_tree_2(list_of_freqs):
    """creates huffman tree from a list of character frequencies.
    Args:
        list_of_freqs (list): list of character frequencies
    Returns:
        (None or HuffmanNode): returns huffman tree
    """
    huff_nodes = []
    if list_of_freqs == [0] * 256:
        return None
    for i, val in enumerate(list_of_freqs):
        if val != 0:
            huff_nodes.append(HuffmanNode(val, chr(i)))
    while len(huff_nodes) > 1:
        x = find_min(huff_nodes)
        huff1 = huff_nodes.pop(x)
        x = find_min(huff_nodes)
        huff2 = huff_nodes.pop(x)
        new_node = HuffmanNode(huff1.freq + huff2.freq, None, huff1, huff2)
        if huff1.char < huff2.char:
            new_node.char = huff1.char
        else:
            new_node.char = huff2.char
        huff_nodes.append(new_node)
    return huff_nodes[find_min(huff_nodes
    )]
    
def find_min(lst):
    min = lst[0]
    min_idx = 0
    for i, val in enumerate(lst):
        if val < min:
            min = val
            min_idx = i
    return i

        


def create_code(root_node):
    """creates huffman code from the huffman tree.
    Args:
        root_node (None or HuffmanNode): root node of huffman tree
    Returns:
        (list): list of codes for all 256 characters
    """
    code_array = [''] * 256
    return create_code_helper(root_node, code_array)


def create_code_helper(root_node, code_array, code=''):
    """creates huffman code from the huffman tree.
    Args:
        root_node (None or HuffmanNode): root node of huffman tree
        code (str): code for character
        code_array (list): list of character codes
    Returns:
        (list): list of codes for all 256 characters
    """
    if root_node is None:
        return code_array
    if root_node.left is None and root_node.right is None:
        code_array[ord(root_node.char)] = code
    create_code_helper(root_node.left, code_array, code + '0')
    create_code_helper(root_node.right, code_array, code + '1')
    return code_array


def create_header(list_of_freqs):
    """creates header for file.
    Args:
        list_of_freqs (list): list of frequencies of characters
    Returns:
        (str): header with ASCII values and corresponding frequencies
    """
    out_str = ''
    for i, val in enumerate(list_of_freqs):
        if val != 0:
            out_str += "%d %d " % (i, val)
    return out_str + "\n"


def huffman_encode(in_file, out_file):
    """fully encodes the input file, Huffman style (BARS).
    Args:
        in_file (str): input file
        out_file (str): encoded output file
    Returns:
        -
    """
    try:
        freqs = cnt_freq(in_file)
    except FileNotFoundError:
        raise FileNotFoundError
    header = create_header(freqs)
    tree = create_huff_tree(freqs)
    codes = create_code(tree)
    new_code = ''
    read_file = open(in_file, "r")
    for line in read_file:
        for ch in line:
            new_code += codes[ord(ch)]
    write_file = open(out_file, "w")
    write_file.write(header)
    write_file.write(new_code)
    read_file.close()
    write_file.close()


def compress_code(in_file, comp_file):
    """compresses a noncompressed file.
    Args:
        in_file (str): input file
        comp_file (str): compressed output file
    Returns:
        -
    """
    file = open(in_file, "r")
    data = file.readlines()
    compressed = HuffmanBitWriter(comp_file)
    compressed.write_str(data[0])
    compressed.write_code(data[1])
    file.close()
    compressed.close()


def huffman_decode(encoded_file, decoded_file):
    """fully decodes the input file, Huffman style (BARS).
    Args:
        encoded_file (str): encoded input file
        decoded_file (str): decoded output file
    Returns:
        -
    """
    comp_file = HuffmanBitReader(encoded_file)
    out_file = open(decoded_file, "w")
    header = comp_file.read_str()
    counts = parse_header(header)
    tree = create_huff_tree(counts)
    out_str = ''
    current_char = None
    while current_char != chr(0):
        current_node = tree
        while current_node.left is not None:
            if comp_file.read_bit():
                current_node = current_node.right
            else:
                current_node = current_node.left
        current_char = current_node.char
        if current_char != chr(0):
            out_str += current_char
    out_file.write(out_str)
    comp_file.close()
    out_file.close()


def parse_header(header_string):
    """converts header of encoded file to array with char frequencies.
    Args:
        header_string (str): header of file
    Returns:
        (list): array of size 256
    """
    counts = [0] * 256
    head = header_string.split()
    for i in range(0, len(head), 2):
        counts[int(head[i])] = int(head[i + 1])
    return counts
