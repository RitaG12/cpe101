import unittest
from fold import *

class TestCases(unittest.TestCase):
   def test_sum1(self):
      list = [4, 2, 7,0]
      self.assertEqual(sum(list), 13)
   def test_sum3(self):
      list = [ ]
      self.assertEqual(sum(list), 0) 
   def test_index_of_smallest1(self):
      list = [4, 2, 7, 0]
      self.assertEqual(index_of_smallest(list), 3)  
   def test_index_of_smallest2(self):
      list = [-1, 3, -4, 4]
      self.assertEqual(index_of_smallest(list), 2)
   def test_index_of_smallest3(self):
      list = [4, 2,  7,2, 3]
      self.assertEqual(index_of_smallest(list), 1)
   def test_index_of_smallest1(self):
      list = [ ]
      self.assertEqual(index_of_smallest(list), -1)
# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

