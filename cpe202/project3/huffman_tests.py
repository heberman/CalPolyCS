"""Tests for Huffman.
Course: CPE202
Quarter: Spring 2020
Author: Henry Berman
"""
import unittest
import filecmp
from huffman_coding import *


class TestCases(unittest.TestCase):
    def test_huffman_node1(self):
        huff1 = HuffmanNode(1, 'a')
        self.assertEqual(str(huff1), '(1, a)')
        huff2 = huff1
        self.assertEqual(huff1, huff2)
        huff3 = HuffmanNode(2, 'b')
        self.assertTrue(huff1 < huff3)
        huff4 = HuffmanNode(1, 'b')
        self.assertTrue(huff1 < huff4)

    def test_cnt_freq(self):
        freqlist = cnt_freq("file1.txt")
        anslist = [0] * 256
        anslist[97:104] = [2, 4, 8, 16, 0, 2, 0]
        self.assertListEqual(freqlist[97:104], anslist[97:104])

    def test_create_huff_tree(self):
        freqlist = cnt_freq("file1.txt")
        hufftree = create_huff_tree(freqlist)
        self.assertEqual(hufftree.freq, 33)
        self.assertEqual(hufftree.left.char, 'd')
        left = hufftree.left
        self.assertEqual(left.freq, 16)
        self.assertEqual(left.char, 'd')
        right = hufftree.right
        self.assertEqual(right.freq, 17)
        self.assertEqual(ord(right.char), 0)

    def test_create_code(self):
        freqlist = cnt_freq("file1.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord('d')], '0')
        self.assertEqual(codes[ord('a')], '11111')
        self.assertEqual(codes[ord('f')], '1110')

    def test_create_header(self):
        freqlist = cnt_freq("file1.txt")
        header = create_header(freqlist)
        self.assertEqual(header, "0 1 97 2 98 4 99 8 100 16 102 2 \n")

    def test_01_encodefile(self):
        huffman_encode("file1.txt", "encodetest4.txt")
        # capture errors by running 'filecmp' on your encoded file
        # with a *known* solution file
        self.assertTrue(filecmp.cmp("encodetest4.txt", "file4_soln.txt"))

    def test_01_decodefile(self):
        huffman_decode("file1_soln_compressed.txt", "decodetest1.txt")
        # capture errors by running 'filecmp' on your encoded file
        # with a *known* solution file
        self.assertTrue(filecmp.cmp("decodetest1.txt", "file1.txt"))


if __name__ == '__main__':
   unittest.main()
