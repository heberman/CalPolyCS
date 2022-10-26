"""Tests for Lab 8 methods.
Course: CPE202
Quarter: Spring 2020
Author: Henry Berman
"""
import unittest
from hashtables import *


class MyTest(unittest.TestCase):
    def test_sepchain1(self):
        table = HashTableSepchain()
        table2 = HashTableSepchain()
        self.assertEqual(table, table2)
        exe = [None] * 11
        self.assertEqual(str(table), str(exe))
        self.assertEqual(table.size(), 0)
        self.assertFalse(table.contains('poop'))
        self.assertEqual(table.load_factor(), 0.0)
        self.assertEqual(table.collisions(), 0)

    def test_sepchain2(self):
        table = HashTableSepchain()
        table['stop'] = 0
        self.assertTrue('stop' in table)
        self.assertEqual(table['stop'], 0)
        self.assertEqual(table.remove('stop'), ('stop', 0))

    def test_linear1(self):
        table = HashTableLinear()
        table2 = HashTableLinear()
        self.assertEqual(table, table2)
        exe = [None] * 11
        self.assertEqual(str(table), str(exe))
        self.assertEqual(table.size(), 0)
        self.assertFalse(table.contains('poop'))
        self.assertEqual(table.load_factor(), 0.0)
        self.assertEqual(table.collisions(), 0)

    def test_linear2(self):
        table = HashTableLinear()
        table['stop'] = 0
        self.assertTrue('stop' in table)
        self.assertEqual(table['stop'], 0)
        self.assertEqual(table.remove('stop'), ('stop', 0))

    def test_quadratic1(self):
        table = HashTableQuadratic()
        table2 = HashTableQuadratic()
        self.assertEqual(table, table2)
        exe = [None] * 16
        self.assertEqual(str(table), str(exe))
        self.assertEqual(table.size(), 0)
        self.assertFalse(table.contains('poop'))
        self.assertEqual(table.load_factor(), 0.0)
        self.assertEqual(table.collisions(), 0)

    def test_quadratic2(self):
        table = HashTableQuadratic()
        table['stop'] = 0
        self.assertTrue('stop' in table)
        self.assertEqual(table['stop'], 0)
        self.assertEqual(table.remove('stop'), ('stop', 0))

    def test_stopwords(self):
        table1 = HashTableSepchain()
        table2 = HashTableLinear()
        table3 = HashTableQuadratic()
        sepchain = import_stopwords('stop_words.txt', table1)
        linear = import_stopwords('stop_words.txt', table2)
        quadratic = import_stopwords('stop_words.txt', table3)
        self.assertTrue('nothing' in sepchain)
        self.assertTrue('nothing' in linear)
        self.assertTrue('nothing' in quadratic)




if __name__ == '__main__':
    unittest.main()
