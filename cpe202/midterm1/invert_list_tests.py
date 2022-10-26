"""Class for Node and function invert_list().
Course: CPE202
Quarter: Spring 2020
Author: Henry Berman
"""

import unittest
from invert_list import *


class TestCases(unittest.TestCase):
    def test1(self):
        n1 = Node(1)
        n2 = Node(1)
        self.assertEqual(n1, n2)
        self.assertEqual(str(n1), 'Node(1, None)')

    def test2(self):
        lst = None
        self.assertEqual(None, invert_list(lst))

    def test3(self):
        lst = Node(3)
        self.assertEqual(Node(3), invert_list(lst))

    def test4(self):
        lst = Node(1, Node(2))
        self.assertEqual(Node(2, Node(1)), invert_list(lst))

    def test5(self):
        lst = Node(1, Node(2, Node(3)))
        self.assertEqual(Node(3, Node(2, Node(1))), invert_list(lst))

if __name__ == '__main__':
    unittest.main()