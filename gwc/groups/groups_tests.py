import unittest
from groups import *


class TestCases(unittest.TestCase):
    def test_groups(self):
        list = [1,2,3,4,5,6,7,8,9,10]
        self.assertFalse(sumHundred(list))

    def test_group1(self):
       list = [1,2,3,50,40,50]
       self.assertTrue(sumHundred(list))
    def test_group2(self):
        list = [1,2,3,30,50,3,3,3,3,3]
        self.assertFalse(sumHundred(list))




# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

