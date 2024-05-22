# Write a Python class named Rectangle constructed by a length and width and a method which will compute the perimeter of a rectangle.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

r = Rectangle(4, 5)
print(r.perimeter())
