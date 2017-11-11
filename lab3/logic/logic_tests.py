import unittest
from logic import *


class TestCases(unittest.TestCase):
   def test_even1(self):
     self.assertTrue(is_even(4))
   def test_even2(self):
     self.assertTrue(is_even(6))

   def test_interval1(self):
      self.assertTrue(is_an_interval(7))

   def test_interval2(self):
      self.assertTrue(is_an_interval(50))

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

