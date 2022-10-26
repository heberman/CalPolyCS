"""Tests for Project 1 functions.
Course: CPE202
Quarter: Spring 2020
Author: Henry Berman
"""


import unittest
from perm_gen_lex import *
from base_convert import *
from bear_picnic import *

class TestCases(unittest.TestCase):

    def test_perm_gen_lex1(self):
        self.assertEqual([], perm_gen_lex(""))

    def test_perm_gen_lex2(self):
        self.assertEqual(["a"], perm_gen_lex("a"))

    def test_perm_gen_lex3(self):
        self.assertEqual(["ab", "ba"], perm_gen_lex("ab"))

    def test_perm_gen_lex4(self):
        self.assertEqual(["abc", "acb", "bac", "bca", "cab", "cba"], perm_gen_lex("abc"))

    def test_convert1(self):
        self.assertEqual("132", convert(30, 4))

    def test_convert2(self):
        self.assertEqual("101101", convert(45, 2))

    def test_convert3(self):
        self.assertEqual("13C", convert(316, 16))

    def test_convert4(self):
        self.assertEqual("120", convert(15, 3))

    def test_bears1(self):
        self.assertTrue(bears(250))

    def test_bears2(self):
        self.assertTrue(bears(42))

    def test_bears3(self):
        self.assertFalse(bears(53))

    def test_bears4(self):
        self.assertFalse(bears(41))


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()