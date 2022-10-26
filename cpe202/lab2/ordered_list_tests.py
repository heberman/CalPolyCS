"""Tests for Lab 2 methods.
Course: CPE202
Quarter: Spring 2020
Author: Henry Berman
"""


import unittest
from ordered_list import *

class TestCases(unittest.TestCase):
    def test_1(self):
        lst = OrderedList()
        self.assertTrue(lst.is_empty())
        lst.add(1)
        self.assertFalse(lst.is_empty())
        lst.add(3)
        self.assertEqual(1, lst.head.val)
        self.assertEqual(3, lst.tail.val)
        lst.add(2)
        self.assertEqual(2, lst.head.next.val)
        self.assertEqual(2, lst.tail.prev.val)

    def test_2(self):
        lst = OrderedList()
        lst.add(1)
        lst.add(2)
        lst.add(3)
        self.assertEqual(1, lst.remove(2))
        self.assertEqual(1, lst.head.val)

    def test_3(self):
        lst = OrderedList()
        lst.add(1)
        lst.add(2)
        self.assertEqual(2, lst.size())
        lst.add(3)
        lst.add(4)
        self.assertEqual(3, lst.remove(4))
        self.assertEqual(3, lst.tail.val)
        self.assertEqual(1, lst.head.val)
        lst.remove(1)
        self.assertEqual(2, lst.head.val)
        self.assertEqual(2, lst.size())
        self.assertRaises(ValueError, lst.remove, 0)

    def test_4(self):
        lst = OrderedList()
        self.assertTrue(lst.is_empty())
        lst.add(1)
        self.assertFalse(lst.is_empty())
        self.assertEqual(0, lst.remove(1))
        self.assertTrue(lst.is_empty())

    def test_5(self):
        lst = OrderedList()
        lst.add(1)
        lst.add(2)
        lst.add(3)
        self.assertTrue(lst.search_forward(1))
        self.assertTrue(lst.search_forward(2))
        self.assertTrue(lst.search_forward(3))
        self.assertFalse(lst.search_forward(0))
        self.assertFalse(lst.search_forward(4))

    def test_6(self):
        lst = OrderedList()
        lst.add(1)
        lst.add(2)
        lst.add(3)
        self.assertTrue(lst.search_backward(1))
        self.assertTrue(lst.search_backward(2))
        self.assertTrue(lst.search_backward(3))
        self.assertFalse(lst.search_backward(0))
        self.assertFalse(lst.search_backward(4))

    def test_7(self):
        lst = OrderedList()
        lst.add(1)
        lst.add(2)
        lst.add(3)
        self.assertEqual(0, lst.index(1))
        self.assertEqual(1, lst.index(2))
        self.assertEqual(2, lst.index(3))
        self.assertRaises(ValueError, lst.index, 0)
        self.assertRaises(ValueError, lst.index, 4)

    def test_8(self):
        lst = OrderedList()
        lst.add(1)
        lst.add(2)
        lst.add(3)
        lst.add(4)
        lst.add(5)
        self.assertEqual(5, lst.pop())
        self.assertEqual(4, lst.tail.val)
        self.assertEqual(1, lst.pop(0))
        self.assertEqual(2, lst.head.val)
        self.assertEqual(3, lst.pop(1))

    def test_9(self):
        lst = OrderedList()
        lst.add(1)
        lst.add(2)
        self.assertRaises(IndexError, lst.pop, 2)
        self.assertEqual(2, lst.pop(1))
        self.assertEqual(1, lst.pop())
        self.assertTrue(lst.is_empty())

    def test_10(self):
        lst = OrderedList()
        lst.add(1)
        lst.add(2)
        lst.add(3)
        lst.add(4)
        lst.add(5)
        self.assertEqual(4, lst.pop(3))

    def test_11(self):
        n1 = Node(1, None, None)
        n2 = Node(1, None, None)
        self.assertEqual(n1, n2)
        lst1 = OrderedList()
        lst1.add(1)
        lst2 = OrderedList()
        lst2.add(1)
        self.assertEqual(lst1, lst2)


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
