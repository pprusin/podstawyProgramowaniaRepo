#Write a Python program that accepts a string and calculates the number of digits and letters.
string = input("Enter a string: ")
numDigits = 0
numLetters = 0

for char in string:
    if char.isdigit():
        numDigits += 1
    elif char.isalpha():
        numLetters += 1

print("Number of digits:", numDigits)
print("Number of letters:", numLetters)
