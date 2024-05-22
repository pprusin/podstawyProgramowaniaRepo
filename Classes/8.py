# Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price):
        self.items[item] = price

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    def total_price(self):
        return sum(self.items.values())

cart = ShoppingCart()
cart.add_item("apple", 1.5)
cart.add_item("orange", 2.0)
print(cart.total_price())
cart.remove_item("apple")
print(cart.total_price())
