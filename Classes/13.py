# Write a Python class named Square constructed by a length and a method which will compute the area of a square.
class Square:
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

s = Square(19)
print(s.area())
