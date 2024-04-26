#Write a Python program to remove spaces from a given string.
def removeSpaces(string):
    return string.replace(" ", "")

input_string = "This is a sample string with spaces."
result = removeSpaces(input_string)
print("String after removing spaces:", result)
