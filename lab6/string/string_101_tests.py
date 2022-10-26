import unittest
from string_101 import *

class TestString(unittest.TestCase):
   def test_str_rot_13_1(self):
      self.assertEqual(str_rot_13("abcNOP"), "nopABC")

   def test_str_rot_13_2(self):
      self.assertEqual(str_rot_13("f5&Nq"), "s5&Ad")

   def test_str_translate_101_1(self):
      self.assertEqual(str_translate_101("abcdabcdaa", "a", "z"), "zbcdzbcdzz")

   def test_str_translate_101_2(self):
      self.assertEqual(str_translate_101("mississippi", "i", "o"), "mossossoppo")


if __name__ == '__main__':
   unittest.main()

