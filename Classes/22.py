# Write a Python class named Dog with attributes like name and age. Include a method to make the dog bark.
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "Woof!"

d = Dog("Tosia", 5)
print(d.bark())
