import math

def distance(p1, p2):
    dist = math.sqrt( (p2.y - p1.y)**2 + (p2.x - p1.x)**2 )
    return dist

def circles_overlap(c1, c2):
    return distance(c1.center, c2.center) < (c1.radius + c2.radius)

