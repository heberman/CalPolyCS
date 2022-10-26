"""Tests for Lab 1 functions.
Course: CPE202
Quarter: Spring 2020
Author: Henry Berman
"""

import unittest
from lab1 import *

class TestCases(unittest.TestCase):
    def test_get_max1(self):
        test_list = []
        self.assertEqual(None, get_max(test_list))

    def test_get_max2(self):
        test_list = [4,8,10,2,-5,7]
        self.assertEqual(10, get_max(test_list))

    def test_get_max3(self):
        test_list = [7,6,5]
        self.assertEqual(7, get_max(test_list))

    def test_reverse1(self):
        test_str = ""
        self.assertEqual("", reverse(test_str))

    def test_reverse2(self):
        test_str = "a"
        self.assertEqual("a", reverse(test_str))

    def test_reverse3(self):
        test_str = "abcxyz"
        self.assertEqual("zyxcba", reverse(test_str))

    def test_binary_search1(self):
        test_list = []
        target = 2
        self.assertEqual(None, binary_search(test_list, target))

    def test_binary_search2(self):
        test_list = [1,3,5]
        target = 2
        self.assertEqual(None, binary_search(test_list, target))

    def test_binary_search3(self):
        test_list = [1,2,5,8,15,22,24,31,40]
        target = 5
        self.assertEqual(2, binary_search(test_list, target))

    def test_binary_search4(self):
        test_list = [1,2,3,4,5,6,7]
        target = 4
        self.assertEqual(3, binary_search(test_list, target))

    def test_binary_search5(self):
        test_list = [1]
        target = 1
        self.assertEqual(0, binary_search(test_list, target))

    def test_fib1(self):
        num = 0
        self.assertEqual(0, fib(num))

    def test_fib2(self):
        num = 1
        self.assertEqual(1, fib(num))

    def test_fib3(self):
        num = 4
        self.assertEqual(3, fib(num))

    def test_fib4(self):
        num = 6
        self.assertEqual(8, fib(num))

    def test_factorial_iter1(self):
        num = 0
        self.assertEqual(1, factorial_iter(num))

    def test_factorial_iter2(self):
        num = 1
        self.assertEqual(1, factorial_iter(num))

    def test_factorial_iter3(self):
        num = 3
        self.assertEqual(6, factorial_iter(num))

    def test_factorial_iter4(self):
        num = 5
        self.assertEqual(120, factorial_iter(num))

    def test_factorial_rec1(self):
        num = 0
        self.assertEqual(1, factorial_rec(num))

    def test_factorial_rec2(self):
        num = 1
        self.assertEqual(1, factorial_rec(num))

    def test_factorial_rec3(self):
        num = 3
        self.assertEqual(6, factorial_rec(num))

    def test_factorial_rec4(self):
        num = 5
        self.assertEqual(120, factorial_rec(num))


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()


