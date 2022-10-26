from objects import *
from math import sqrt

def distance(p1, p2):
    return sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)

def circles_overlap(c1, c2):
    return distance(c1.center, c2.center) < (c1.radius + c2.radius)