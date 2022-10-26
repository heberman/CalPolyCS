import unittest
from char import *

class TestChar(unittest.TestCase):
   def test_lower_1(self):
      self.assertEqual(is_lower_101('a'), True)

   def test_lower_2(self):
      self.assertEqual(is_lower_101('M'), False)

   def test_lower_3(self):
      self.assertEqual(is_lower_101('z'), True)

   def test_char_rot_13_1(self):
      self.assertEqual(char_rot_13('a'), 'n')

   def test_char_rot_13_2(self):
      self.assertEqual(char_rot_13('w'), 'j')

   def test_char_rot_13_3(self):
      self.assertEqual(char_rot_13('B'), 'O')

   def test_char_rot_13_4(self):
      self.assertEqual(char_rot_13('N'), 'A')

   def test_char_rot_13_5(self):
      self.assertEqual(char_rot_13('#'), '#')

if __name__ == '__main__':
   unittest.main()

