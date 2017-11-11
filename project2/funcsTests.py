import unittest
from landerFuncs import *

class TestCases(unittest.TestCase):
   def test_update_acc1(self):
      self.assertAlmostEqual(updateAcceleration(1.62, 0), -1.62)
   def test_update_acc2(self):
      self.assertEqual(updateAcceleration(1.62, 5), 0)

   def test_update_alt1(self):
      self.assertEqual(updateAltitude(5,3,6), 11)
   def test_update_alt2(self):
      self.assertEqual(updateAltitude(3,0,2), 4)

   def test_vel1(self):
      self.assertEqual(updateVelocity(0,4), 4)
   def test_vel2(self):
      self.assertEqual(updateVelocity(.5,5), 5.5)

   def test_update_fuel1(self):
      self.assertEqual(updateFuel(0,6), -6)
   def test_update_fuel2(self):
      self.assertEqual(updateFuel(17,5), 12) 
   
   

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

