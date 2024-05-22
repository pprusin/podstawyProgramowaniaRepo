# Write a Python class named Employee with two attributes: name and salary. Include a method to calculate a bonus.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self, percentage):
        return self.salary * percentage / 100

e = Employee("Piotr", 2313132421)
print(e.calculate_bonus(10))
