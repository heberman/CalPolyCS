import unittest
from landerFuncs import *

class TestCases(unittest.TestCase):
   def test_update_acc1(self):
      self.assertAlmostEqual(updateAcceleration(1.62, 0), -1.62)

   def test_update_acc2(self):
      for i in range(0, 9):
         self.assertAlmostEqual(updateAcceleration(1.62, i), (1.62 * (i/5 - 1)))

   def test_update_acc3(self):
      self.assertAlmostEqual(updateAcceleration(2.345, 6), .469)

   def test_update_acc4(self):
      self.assertAlmostEqual(updateAcceleration(9.8, 8), 5.88)

   def test_update_alt1(self):
      self.assertAlmostEqual(updateAltitude(100, -2.4, -1.62), 96.79)

   def test_update_alt2(self):
      self.assertAlmostEqual(updateAltitude(690, 6.9, -4.20), 694.8)

   def test_update_alt3(self):
      self.assertAlmostEqual(updateAltitude(4269, -8.8, .2), 4260.3)

   def test_update_alt4(self):
      self.assertAlmostEqual(updateAltitude(10, -8, -5), 0)

   def test_update_velo1(self):
      self.assertAlmostEqual(updateVelocity(8.69, 4.21), 12.90)

   def test_update_velo2(self):
      self.assertAlmostEqual(updateVelocity(0, .1), .1)

   def test_update_velo3(self):
      self.assertAlmostEqual(updateVelocity(3.6, 0.01), 3.61)

   def test_update_fuel1(self):
      self.assertEqual(updateFuel(8, 4), 4)

   def test_update_fuel2(self):
      self.assertEqual(updateFuel(2, 2), 0)

   def test_update_fuel3(self):
      self.assertEqual(updateFuel(200, 9), 191)
      

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

