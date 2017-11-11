import unittest
from funcs import *

class Tests(unittest.TestCase):
   def test_pounds1(self): #do we need a new method for each test case? 
       self.assertAlmostEqual(poundsToKG(140),63.502880000)
   def test_pounds1(self):
       self.assertAlmostEqual(poundsToKG(1),0.453592000000) 

   def test_getMass1(self):
       self.assertEqual(getMassObject('t'),0.1)
   def test_getMass2(self):
       self.assertEqual(getMassObject('p'),1.0)
   def test_getMass3(self):
       self.assertEqual(getMassObject('r'),3.0)
   def test_getMass4(self):
       self.assertEqual(getMassObject('g'),5.3)
   def test_getMass5(self):
       self.assertEqual(getMassObject('l'),9.07) #put in string

   def test_getVelObject1(self):
       self.assertAlmostEqual(getVelocityObject(10), 7)
   def test_getVelObject2(self):
       self.assertAlmostEqual(getVelocityObject(1),2.213594362)
   def test_getVelObject3(self):
       self.assertAlmostEqual(getVelocityObject(0), 0.0)  
 
   def test_velSkater1(self):
       self.assertAlmostEqual(getVelocitySkater(poundsToKG(100), 3.0, getVelocityObject(50)), 1.035234914)
   def test_velSkater2(self):
       self.assertAlmostEqual(getVelocitySkater(poundsToKG(50), 5.3, getVelocityObject(11)), 1.715674362) 
  
if __name__ == '__main__':
   unittest.main()
