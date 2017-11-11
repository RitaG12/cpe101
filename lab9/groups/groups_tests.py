import unittest
from groups import *


class TestCases(unittest.TestCase):
    def test_groups(self):
        list = [1,2,3,4,5,6,7,8,9]
        ans = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(groups_of_3(list),ans)
    def test_group1(self):
        list = [1,2,3,4,5]
        ans= [[1,2,3],[4,5]]
        self.assertEqual(groups_of_3(list), ans)
    def test_group2(self):
        list = [3,4,5,6,7,8,9,10,11,12]
        ans= [[3,4,5],[6,7,8],[9,10,11],[12]]
        self.assertEqual(groups_of_3(list), ans)





# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

