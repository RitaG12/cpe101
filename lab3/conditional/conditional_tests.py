import unittest
from conditional import *

class TestCases(unittest.TestCase):
   def test_max101_1(self):
      self.assertEqual(max_101(2,10), 10)

   def test_max101_2(self):
       self.assertEqual(max_101(7,3), 7)
       self.assertEqual(max_101(5,5), 5)

   def test_max_of_three1(self):
       self.assertEqual(max_of_three(20.2, 20.3, 4.2), 20.3)
   def test_max_of_three2(self):
       self.assertEqual(max_of_three(50.06, 21.6, 53), 53)
   def test_max_of_three3(self):
       self.assertEqual(max_of_three(2,5,5), 5)  
   def test_max_of_three4(self):
       self.assertEqual(max_of_three(5,5,1), 5)  
 
   def test_rental1(self):
       self.assertEqual(rental_late_fee(0), 0)
   def test_rental2(self):
       self.assertEqual(rental_late_fee(4), 5)
   def test_rental3(self):
       self.assertEqual(rental_late_fee(12), 7)
   def test_rental4(self):
       self.assertEqual(rental_late_fee(20), 19)
   def test_rental5(self):
       self.assertEqual(rental_late_fee(30), 100)




# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

