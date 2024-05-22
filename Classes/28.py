# Write a Python class named Distance with a method to convert miles to kilometers.
class Distance:
    def __init__(self, miles):
        self.miles = miles

    def to_kilometers(self):
        return self.miles * 1.60934

d = Distance(10)
print(d.to_kilometers())
