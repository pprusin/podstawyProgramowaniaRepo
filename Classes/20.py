# Write a Python class named Book with attributes like title and price. Include a method to display the price.
class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def display_price(self):
        return self.price

b = Book("Szczebrzeszyn", 29.99)
print(b.display_price())
