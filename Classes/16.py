# Write a Python class named BankAccount with methods to deposit and withdraw money. Include a method to display the balance.
class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            return "Insufficient balance"

    def display_balance(self):
        return self.balance

account = BankAccount()
account.deposit(100)
account.withdraw(30)
print(account.display_balance())
