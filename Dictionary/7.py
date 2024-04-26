# Write a Python program to get a dictionary from an object's fields.
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

personObject = Person("Alice", 30, "New York")

personDict = vars(personObject)

print("Dictionary from object's fields:")
print(personDict)
