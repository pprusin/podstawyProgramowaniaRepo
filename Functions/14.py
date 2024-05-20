#Write a Python function that takes two arguments, and returns True if the first number is divisible by the second number.
def is_divisible(a, b):
    return a % b == 0

print(is_divisible(4,2))