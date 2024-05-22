# Write a Python class named BankAccount with methods to deposit, withdraw money and calculate interest.
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

    def calculate_interest(self, rate):
        return self.balance * rate / 100

account = BankAccount()
account.deposit(1000)
print(account.calculate_interest(5))
