import unittest
from poly import *

class TestPoly(unittest.TestCase):

   def assertListAlmostEqual(self, l1, l2):
      self.assertEqual(len(l1), len(l2))
      for el1, el2 in zip(l1, l2):
         self.assertAlmostEqual(el1, el2)

   def test_polyadd2_1(self):
       poly1 = [5.0, 4.3, 6.2]
       poly2 = [1.1, 3.5, 6.4]

       poly3 = poly_add2(poly1, poly2)
       self.assertListAlmostEqual(poly3, [6.1, 7.8,12.6])

   def test_polyadd2_2(self):
       poly1 = [0, 3, 4]
       poly2 = [5.3, 0, -2]

       poly3 = poly_add2(poly1, poly2)
       self.assertListAlmostEqual(poly3, [5.3, 3, 2])

   def test_mult2_1(self):
       poly1 = [2, 1, 4]
       poly2 = [4, 1, 3]

       poly3 = poly_mult2(poly1, poly2)
       self.assertListAlmostEqual(poly3, [8, 6, 23, 7, 12]) 

   def test_mult2_2(self):
       poly1 = [0,1,3]
       poly2 = [4, 3.4, 0]

       poly3 = poly_mult2(poly1, poly2)
       self.assertListAlmostEqual(poly3, [0, 4, 15.4, 10.2, 0])  

   def test_mult3(self):
       poly1 = [1,0,0]
       poly2 = [2,0,0]
       poly3 = poly_mult2(poly1,poly2)
       self.assertListAlmostEqual(poly3, [2,0,0,0,0])

  # Add tests here

if __name__ == '__main__':
   unittest.main()
