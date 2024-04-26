#Write a Python program that accepts a sequence of comma separated 4 digit binary numbers as its input. The program will print the numbers that are divisible by 5 in a comma separated sequence.
binary_numbers = input("Enter comma-separated 4-digit binary numbers: ").split(',')

divisible_by_5 = []

for binary in binary_numbers:
    decimal = int(binary, 2)
    if decimal % 5 == 0:
        divisible_by_5.append(binary)

print("Numbers divisible by 5:", ','.join(divisible_by_5))
