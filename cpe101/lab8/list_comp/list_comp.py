from objects import *
from math import sqrt

def distance(p1, p2):
    return sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)

def distance_all(points):
    return [distance(Point(0,0), point) for point in points]

def are_in_first_quadrant(points):
    return [point for point in points if point.x > 0 and point.y > 0]