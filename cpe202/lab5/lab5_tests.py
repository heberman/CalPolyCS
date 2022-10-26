"""Tests for Lab 5 methods.
Course: CPE202
Quarter: Spring 2020
Author: Henry Berman
"""


import unittest
from tree_map import *
from bst import *


class MyTest(unittest.TestCase):

    def test_BSTNode1(self):
        tree = None
        tree = insert(tree, 4, 'four')
        tree = insert(tree, 2, 'two')
        tree = insert(tree, 3, 'three')
        tree = insert(tree, 7, 'seven')
        tree = insert(tree, 1, 'one')
        tree = insert(tree, 5, 'five')
        tree = insert(tree, 6, 'six')
        self.assertEqual(tree.right.left.right.key, 6)
        self.assertEqual(tree.right.key, 7)
        self.assertEqual(tree.left.key, 2)
        self.assertEqual(tree_height(tree), 3)
        tree = delete(tree, 6)
        self.assertEqual(tree.key, 4)
        self.assertEqual(tree.left.key, 2)
        self.assertEqual(tree.right.key, 7)
        self.assertEqual(tree.right.left.key, 5)
        self.assertEqual(tree_height(tree), 2)
        self.assertEqual(find_min(tree), (1, 'one'))
        self.assertEqual(find_max(tree), (7, 'seven'))

    def test_BSTNode2(self):
        tree1 = TreeMap()
        tree2 = TreeMap()
        tree1.put(1, 1)
        tree2.put(1, 1)
        self.assertEqual(tree1, tree2)
        self.assertTrue(1 in tree1)
        self.assertEqual(tree1.get(1), 1)
        self.assertEqual(tree1[1], 1)
        tree1[0] = 2
        self.assertEqual(tree1.get(0), 2)
        tree2.delete(1)
        self.assertEqual(tree2.size(), 0)
        self.assertEqual(tree2.tree, None)
        tree2.put(2, 2)
        tree2.put(1, 1)
        tree2.put(3, 3)
        self.assertEqual(tree2.tree.val, 2)
        self.assertEqual(tree2.find_min(), (1, 1))
        self.assertEqual(tree2.find_max(), (3, 3))
        self.assertEqual(tree2.inorder_list(), [1, 2, 3])
        self.assertEqual(tree2.preorder_list(), [2, 1, 3])
        tree2.put(4, 4)
        tree2.put(5, 5)
        self.assertEqual(tree2.tree_height(), 3)
        self.assertEqual(tree2.range_search(1, 4), [(1, 1), (2, 2), (3, 3)])

    def test_classmates(self):
        filename = '/Users/henry/Documents/CS/cpe202/lab5/classmates.tsv'
        tree = import_classmates(filename)
        self.assertNotEqual(search_classmate(tree, 24), search_classmate(tree, 23))
        self.assertEqual(str(search_classmate(tree, 24)),
                                "Classmate{sid: 24, last: Soderquist, first: Drew Edward, major: CPE, year: Junior}")
        self.assertRaises(KeyError, search_classmate, tree, 0)
        self.assertEqual(tree.size(), 52)
        student = search_classmate(tree, 24)
        self.assertEqual(student.major, 'CPE')


if __name__ == '__main__':
    unittest.main()
