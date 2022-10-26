import unittest
from objects import *
from funcs_objects import *

class TestCases(unittest.TestCase):
   def test_point1(self):
      p = Point(2,3)
      self.assertEqual(p.x, 2)
      self.assertEqual(p.y, 3)

   def test_point2(self):
      p = Point(-1.3,4.9)
      self.assertAlmostEqual(p.x, -1.3)
      self.assertAlmostEqual(p.y, 4.9)

   def test_circle1(self):
      p = Point(1,2)
      c = Circle(p, 3)
      self.assertEqual(c.center.x, 1)
      self.assertEqual(c.center.y, 2)
      self.assertEqual(c.radius, 3)

   def test_distance1(self):
      p1 = Point(0,0)
      p2 = Point(3,4)
      self.assertAlmostEqual(distance(p1,p2), 5.0)

   def test_distance2(self):
      p1 = Point(0,0)
      p2 = Point(-5, -12)
      self.assertAlmostEqual(distance(p1,p2), 13.0)

   def test_circles_overlap1(self):
      c1 = Circle(Point(0,0), 1)
      c2 = Circle(Point(1,1), 10)
      self.assertTrue(circles_overlap(c1, c2))

   def test_circles_overlap2(self):
      c1 = Circle(Point(1,1), 1)
      c2 = Circle(Point(-2,-2), 2)
      self.assertFalse(circles_overlap(c1, c2))

   def test_circles_overlap3(self):
      c1 = Circle(Point(0,0), 1)
      c2 = Circle(Point(3,0), 1)
      self.assertFalse(circles_overlap(c1, c2))

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

