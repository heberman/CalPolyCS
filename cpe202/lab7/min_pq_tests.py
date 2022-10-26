"""Tests for Lab 7 methods.
Course: CPE202
Quarter: Spring 2020
Author: Henry Berman
"""

import unittest
from min_pq import *

class MyTest(unittest.TestCase):
    def test1(self):
        heap = MinPQ()
        self.assertTrue(heap.is_empty())
        heap.insert(4)
        self.assertEqual(heap.min(), 4)
        heap.insert(2)
        self.assertEqual(heap.min(), 2)
        self.assertEqual(heap.size(), 2)
        heap.insert(5)
        self.assertFalse(heap.is_empty())
        heap.insert(3)
        self.assertEqual(heap.min(), 2)
        heap.insert(1)
        self.assertEqual(heap.min(), 1)
        self.assertEqual(heap.arr, [1, 2, 5, 4, 3])
        self.assertEqual(heap.size(), 5)

    def test2(self):
        heap = MinPQ()
        self.assertTrue(heap.is_empty())
        heap.insert(1)
        heap.insert(2)
        self.assertFalse(heap.is_empty())
        heap.insert(3)
        self.assertEqual(heap.del_min(), 1)
        heap.insert(4)
        heap.insert(5)
        self.assertEqual(heap.del_min(), 2)
        self.assertEqual(heap.num_items, 3)


if __name__ == '__main__':
    unittest.main()
