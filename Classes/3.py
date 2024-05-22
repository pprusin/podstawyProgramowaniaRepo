# Write a Python program to create a calculator class. Include methods for basic arithmetic operations.
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"

calc = Calculator()
print(calc.add(2, 3))
print(calc.subtract(7, 5))
print(calc.multiply(3, 4))
print(calc.divide(10, 2))
