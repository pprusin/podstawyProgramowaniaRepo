# Write a Python class named Point representing a point in a 2D space. Include a method to calculate the distance from another point.
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

p1 = Point(1, 2)
p2 = Point(4, 6)
print(p1.distance(p2))
