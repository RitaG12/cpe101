from objects import *
from funcs_objects import *

def distance_all(inputList):
    p1 = Point(0,0)
    outList = [distance(p1,p2) for p2 in inputList]
    return outList

def are_in_first_quadrant(inputList):
    outList = [ p for p in inputList if p.x > 0 and p.y >0]


