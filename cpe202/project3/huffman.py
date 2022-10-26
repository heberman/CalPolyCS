"""Class: HuffmanNode.
Course: CPE202
Quarter: Spring 2020
Author: Henry Berman
"""


class HuffmanNode:
    """HuffmanTree is one of None or HuffmanNode.
    Attributes:
        freq (int): frequency of character in a file
        char (str): a character
        left (None or HuffmanNode): left subtree of HuffmanTree
        right (None or HuffmanNode): right subtree of HuffmanTree
    """
    def __init__(self, freq, char=None, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right

    def __eq__(self, other):
        return self.freq == other.freq and \
               self.char == other.char and \
               self.left == other.left and \
               self.right == other.right

    def __repr__(self):
        return "(%d, %s)" % (self.freq, self.char)

    def __lt__(self, other):
        if self.freq == other.freq:
            return ord(self.char) < ord(other.char)
        return self.freq < other.freq
