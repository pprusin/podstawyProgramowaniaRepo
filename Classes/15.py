# Write a Python class named Employee with two attributes: name and salary. Include a method to display the salary.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_salary(self):
        return self.salary

e = Employee("Piotrek", 121782717289127127)
print(e.display_salary())
