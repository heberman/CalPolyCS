"""Tests for Project 2 functions.
Course: CPE202
Quarter: Spring 2020
Author: Henry Berman
"""

import unittest
from exp_eval import *

class TestCases(unittest.TestCase):
    def test_postfix_eval1(self):
        exp = '1 2 +'
        self.assertEqual(3, postfix_eval(exp))

    def test_postfix_eval2(self):
        exp = '1 0 /'
        self.assertRaises(ValueError, postfix_eval, exp)

    def test_postfix_eval3(self):
        exp = '5 1 2 + 4 ^ + 3 -'
        self.assertEqual(83, postfix_eval(exp))

    def test_postfix_eval4(self):
        exp = '5 6 2 ^ 2 - *'
        self.assertEqual(170, postfix_eval(exp))

    def test_postfix_eval5(self):
        exp = '2 1 4 2 1 + * 3 + + *'
        self.assertEqual(32, postfix_eval(exp))

    def test_postfix_eval6(self):
        exp = '18 3 / 2 ^ 13 7 + 5 2 ^ * +'
        self.assertEqual(536, postfix_eval(exp))

    def test_postfix_eval7(self):
        exp = '1 2 3 - 4 + / 5 6 - * 7 *'
        self.assertAlmostEqual(-2.3333333, postfix_eval(exp))

    def test_postfix_eval8(self):
        exp = '1 2 + 3 + 6 7 * - 4 1 / -'
        self.assertAlmostEqual(-40, postfix_eval(exp))

    def test_infix_to_postfix0(self):
        infix = '6 - 3'
        self.assertEqual('6 3 -', infix_to_postfix(infix))

    def test_infix_to_postfix1(self):
        infix = '1 + 2 + 3 - 6 * 7 - 4 / 1'
        self.assertEqual('1 2 + 3 + 6 7 * - 4 1 / -', infix_to_postfix(infix))

    def test_infix_to_postfix2(self):
        infix = '( ( 2 * ( 3 + 4 ) ) / 5 )'
        self.assertEqual('2 3 4 + * 5 /', infix_to_postfix(infix))

    def test_infix_to_postfix3(self):
        infix = '6 * ( 4 * ( 6 - 2 ) / 8 ) ^ 2'
        self.assertEqual('6 4 6 2 - * 8 / 2 ^ *', infix_to_postfix(infix))

    def test_infix_to_postfix4(self):
        infix = '( 5 - 3 ) ^ 2 ^ 2 ^ 2'
        self.assertEqual('5 3 - 2 2 2 ^ ^ ^', infix_to_postfix(infix))

    def test_prefix_to_postfix1(self):
        prefix = '+ + 4 * 1 2 3'
        self.assertEqual('4 1 2 * + 3 +', prefix_to_postfix(prefix))

    def test_prefix_to_postfix2(self):
        prefix = '- + / 2 ^ 3 4 * 5 6 * 2 4'
        self.assertEqual('2 3 4 ^ / 5 6 * + 2 4 * -', prefix_to_postfix(prefix))


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()