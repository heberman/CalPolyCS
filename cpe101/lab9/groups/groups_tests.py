import unittest
from groups import *

class TestCases(unittest.TestCase):
    def test_groups_1(self):
        x = [1,2,3,4,5,6,7,8,9]
        self.assertEqual(groups_of_3(x), [[1,2,3],[4,5,6],[7,8,9]])

    def test_groups_2(self):
        x = [2,4,6,8,10]
        self.assertEqual(groups_of_3(x), [[2,4,6],[8,10]])

    def test_groups_3(self):
        x = [1,3,5,7,9,11,13,15,17,19]
        self.assertEqual(groups_of_3(x), [[1,3,5],[7,9,11],[13,15,17],[19]])

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()