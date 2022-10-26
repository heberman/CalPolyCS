import unittest
from strspn import *

class TestCases(unittest.TestCase):
   def test_my_strspn_01(self):
      self.assertEqual(3, my_strspn("calpoly", "local"))

   def test_my_strspn_02(self):
      self.assertEqual(3, my_strspn("trail", "backtrack"))

   def test_my_strspn_03(self):
      self.assertEqual(0, my_strspn("break", "mississippi"))

   def test_my_strspn_04(self):
      self.assertEqual(3, my_strspn("tip", "pitfall"))

   def test_my_strspn_05(self):
      self.assertEqual(5, my_strspn("seven", "elevens"))

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()