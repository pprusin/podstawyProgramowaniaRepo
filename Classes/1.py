# Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

c = Circle(5)
print(c.area())
print(c.perimeter())
