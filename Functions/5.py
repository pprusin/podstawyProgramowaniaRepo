#Write a Python function to calculate the factorial of a number (a non-negative integer).
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

print(factorial(3))