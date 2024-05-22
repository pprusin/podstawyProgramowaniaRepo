# Write a Python class named ComplexNumber constructed by two numbers and a method which will compute the addition of two complex numbers.
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def add(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

c1 = ComplexNumber(6,8)
c2 = ComplexNumber(4, 7)
c3 = c1.add(c2)
print(c3.real, "+", c3.imag, "i")
