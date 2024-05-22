# Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.
from datetime import date

class Person:
    def __init__(self, name, country, birthdate):
        self.name = name
        self.country = country
        self.birthdate = birthdate

    def age(self):
        today = date.today()
        return today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))

p = Person("Piotr Prusinowski", "Polska", date(2003, 4, 24))
print(p.age())
