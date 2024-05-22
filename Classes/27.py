# Write a Python class named Temperature with a method to convert Celsius to Fahrenheit.
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32

t = Temperature(27)
print(t.to_fahrenheit())
