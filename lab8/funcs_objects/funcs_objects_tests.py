import unittest
from objects import *
from funcs_objects import *

class TestCases(unittest.TestCase):
    def test_point(self):
        point1 = Point(5,10)
        self.assertEqual(point1.x,5)
        self.assertEqual(point1.y,10)


    def test_circle(self):
        centerPoint = Point(2,5)
        circle = Circle(centerPoint, 7)
        self.assertEqual(circle.center, centerPoint)
        self.assertEqual(circle.radius, 7)

    def distance1(self):
        p1 = Point(0,5)
        p2 = Point(3,0)
        self.assertAlmostEqual(distance(p1, p2), 5.830951845301)
        
    def distance2(self):
        p1 = Point(-1,6)
        p2 = Point(5,1)
        self.assertAlmostEqual(distance(p1, p2), 7.810249675906654)

    def overlap1(self):
        p1 = Point(0,0)
        p2 = Point(10,0)
        c1 = Circle(p1, 5)
        c2 = Circle(p2, 5)
        self.assertFalse(circles_overlap(c1, c2))

    def overlap2(self):
        p1 = Point(0,0)
        p2 = Point(10,0)
        c1 = Circle(p1, 11)
        c2 = Circle(p2, 5)
        self.assertTrue(circles_overlap(c1, c2))

    def overlap3(self):
        p1 = Point(1,1)
        p2 = Point(1,10)
        c1 = Circle(p1, 10)
        c2 = Circle(p2, 4)
        self.assertTrue(circles_overlap(c1, c2))




   # Add other testing functions


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

