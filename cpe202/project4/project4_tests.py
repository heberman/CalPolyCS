"""Tests for Project 3 methods.
Course: CPE202
Quarter: Spring 2020
Author: Henry Berman
"""
import unittest
from project4 import *


class MyTest(unittest.TestCase):
    def test_search_engine1(self):
        stop_table = HashTableQuadratic()
        stopwords = import_stopwords('stop_words.txt', stop_table)
        search_engine = SearchEngine('docs/', stopwords)
        expected = [('docs/test.txt', 1.0), ('docs/information_retrieval.txt', 0.017), ('docs/hash_table.txt', 0.01)]
        self.assertEqual(search_engine.search('computer science'), expected)


if __name__ == '__main__':
    unittest.main()