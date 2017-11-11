import unittest
from list_comp import *
from objects import *
from funcs_objects import *

class TestCases(unittest.TestCase):
    def distance_1(self):
        input = [Point(0,5), Point(6,0), Point(0,0),Point(-3,4)]
        output = [5, 6, 5]
        self.assertEqual(distance_all(input), output)
    def distance_1(self):
        input = [Point(0,5), Point(6,0), Point(0,0),Point(-3,4)]
        output = [5, 6, 5]
        self.assertEqual(distance_all(input), output)

    def quadrant1(self):
        input = [Point(5,5), Point(-3,0), Point(6,7)]
        output = [True, False, True]
        self.assertEqual(are_in_first_quadrant(input), output)
    def quadrant2(self):
        input = [Point(-4,-5), Point(3,3), Point(-3,8)]
        output = [False, True, False]
        self.assertEqual(are_in_first_quadrant(input), output)




# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

