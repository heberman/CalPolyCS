import unittest
from objects import *

class TestCases(unittest.TestCase):
   def test_equality1(self):
      p1 = Point(1,2)
      p2 = Point(1,2)
      self.assertEqual(p1, p2)

   def test_equality2(self):
      p1 = Point(1,2)
      p2 = Point(1,3)
      self.assertNotEqual(p1, p2)


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

