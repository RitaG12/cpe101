from utility import *

class Point:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        if epsilon_equal(self.x, other.x) and epsilon_equal(self.y, other.y):
            return True
        else:
            return False

class Circle:
    def __init__(self, center_Point, radius):
        self.center = center_Point
        self.radius = radius




