#Write a Python program to print the following numbers up to 2 decimal places.
numbers = [3.14159, 1.61803398875, 2.71828, 0.5772156649, 1.41421]

for number in numbers:
    print("{:.2f}".format(number))
