import unittest
from objects import *
from funcs_objects import *

class TestCases(unittest.TestCase):
   def test_point(self):
      p = Point(0,0)
      self.assertEqual(p.x, 0)

   def test_circle(self):
      c = Circle(Point(0,0), 0)
      self.assertEqual(c.center.y, 0)
      self.assertEqual(c.radius, 0)

   def test_distance(self):
      p1 = Point(0,0)
      p2 = Point(3,4)
      self.assertAlmostEqual(distance(p1,p2), 5.0)

   def test_circles_overlap(self):
      c1 = Circle(Point(0,0), 1)
      c2 = Circle(Point(1,1), 10)
      self.assertTrue(circles_overlap(c1, c2))


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

