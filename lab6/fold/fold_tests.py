import unittest
from fold import *

class TestCases(unittest.TestCase):
   def test_sum1(self):
      a = [1,2,3,4]
      self.assertEqual(sum(a), 10)

   def test_sum2(self):
      a = [-3,4,6.7,-91]
      self.assertAlmostEqual(sum(a), -83.3)

   def test_index_of_smallest1(self):
      a = []
      self.assertEqual(index_of_smallest(a), -1)

   def test_index_of_smallest2(self):
      a = [-1,2,-5,69,-420]
      self.assertEqual(index_of_smallest(a), 4)

   def test_index_of_smallest3(self):
      a = [2,2,1,1,3,3]
      self.assertEqual(index_of_smallest(a), 2)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

