import unittest
from filter import *

class TestCases(unittest.TestCase):
   def are_pos_1(self):
      l1 = [-3, 4, 0, -2]
      self.assertEqual(are_positive(l1), [4,0])

   def are_pos_2(self):
      l1 = [-4, 2, 5, 11, 40]
      self.assertEqual(are_positive(l1), [2, 5, 11, 40])

   def are_greater_1(self):
      l1 = [2,5,-4,7]
      self.assertEqual(are_greater_than_n(l1,2), [5, 7])

   def are_greater_2(self):
      l1 = [0,-4,3,79]
      self.assertEqual(are_greater_than_n(l1,0), [3, 79])

   def are_divisible(self):
      l1 = [4,3,2,0,6]
      self.assertEqual(are_divisible_by_n(l1, 2), [4, 2, 0, 6])

   def are_divisible_2(self):
      l1 = [4,8,3,16]
      self.assertEqual(are_divisible_by_n(l1,4), [4, 8, 16]) 

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

