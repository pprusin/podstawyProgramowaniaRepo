# Write a Python class named Person with attributes like name and age. Include a method to display a greeting message.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

p = Person("Piotrek", 21)
print(p.greet())
