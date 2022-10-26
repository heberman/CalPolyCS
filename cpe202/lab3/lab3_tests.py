"""Tests for Lab 3 methods.
Course: CPE202
Quarter: Spring 2020
Author: Henry Berman
"""


import unittest
from stack_array import *
from stack_linked import *

class TestCases(unittest.TestCase):
    def test_stack_array1(self):
        s1 = StackArray()
        self.assertEqual(s1.arr, [None, None])
        self.assertEqual(s1.capacity, 2)
        self.assertEqual(s1.num_items, 0)
        self.assertRaises(IndexError, s1.pop)
        self.assertRaises(IndexError, s1.peek)
        self.assertTrue(s1.is_empty())

    def test_stack_array2(self):
        s1 = StackArray()
        s2 = StackArray()
        self.assertEqual(s1, s2)
        s1.push(1)
        s2.push(1)
        self.assertEqual(s1, s2)
        self.assertEqual(str(s1), '[1, None]')

    def test_stack_array3(self):
        s1 = StackArray()
        self.assertEqual(s1.size(), 0)
        s1.push(1)
        s1.push(2)
        self.assertEqual(s1.size(), 2)
        s1.push(3)
        s1.push(4)
        self.assertEqual(s1.size(), 4)
        self.assertFalse(s1.is_empty())
        self.assertEqual(s1.peek(), 4)
        self.assertEqual(s1.num_items, 4)
        self.assertEqual(s1.pop(), 4)
        self.assertEqual(s1.pop(), 3)
        self.assertEqual(s1.peek(), 2)
        self.assertEqual(s1.pop(), 2)
        self.assertEqual(s1.pop(), 1)
        self.assertTrue(s1.is_empty())

    def test_stack_linked1(self):
        s1 = StackLinked()
        self.assertEqual(s1.top, None)
        self.assertEqual(s1.num_items, 0)
        self.assertRaises(IndexError, s1.pop)
        self.assertRaises(IndexError, s1.peek)
        self.assertTrue(s1.is_empty())

    def test_stack_linked2(self):
        s1 = StackLinked()
        s2 = StackLinked()
        self.assertEqual(s1, s2)
        s1.push(1)
        s2.push(1)
        self.assertEqual(s1, s2)
        self.assertEqual(str(s1), 'Node(1, None)')

    def test_stack_linked3(self):
        s1 = StackLinked()
        self.assertEqual(s1.size(), 0)
        s1.push(1)
        s1.push(2)
        self.assertEqual(s1.size(), 2)
        s1.push(3)
        s1.push(4)
        self.assertEqual(s1.size(), 4)
        self.assertFalse(s1.is_empty())
        self.assertEqual(s1.peek(), 4)
        self.assertEqual(s1.num_items, 4)
        self.assertEqual(s1.pop(), 4)
        self.assertEqual(s1.pop(), 3)
        self.assertEqual(s1.peek(), 2)
        self.assertEqual(s1.pop(), 2)
        self.assertEqual(s1.pop(), 1)
        self.assertTrue(s1.is_empty())


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()