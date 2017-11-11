import unittest
from map import *

class TestCases(unittest.TestCase):
   def square_test_1(self):
      list = [3, 2, 1]
      self.assertEqual(square_all(list), [9, 4, 1])

   def square_test_2(self):
      list = [0, -2, 4]
      self.assertEqual(square_all(list), [0, 4, 16])

   def add_n_1(self):
      list = [10,4,5]
      self.assertEqual(2,add_n_all(list), [12, 6, 7])
  
   def add_n_2(self):
      list = [0, -3, 5]
      self.assertEqual(1,add_n_all(list), [1, -2, 6])

   def even_1(self):
      list = [0, 4, 3]
      self.assertEqual(even_or_odd_all(list), [True, True, False])
 
   def even_2(self):
      list = [-1, 5, 4, -2]
      self.assertEqual(even_or_odd_all(list), [False, False, True, True])

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

