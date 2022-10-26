import unittest
from list_comp import *
from objects import *

class TestCases(unittest.TestCase):
   def test_distance_all(self):
      p1 = Point(0,0)
      p2 = Point(3,4)
      p3 = Point(5,12)
      pts = [p1,p2,p3]
      self.assertEqual(distance_all(pts), [0.0, 5.0, 13.0])

   def test_are_in_first_quadrant(self):
      p1 = Point(0,0)
      p2 = Point(1,1)
      p3 = Point(1,-2)
      pts = [p1,p2,p3]
      self.assertEqual(are_in_first_quadrant(pts), [p2])


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

