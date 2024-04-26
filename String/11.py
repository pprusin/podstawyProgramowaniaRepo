#Write a Python program to remove characters that have odd index values in a given string.
def removeOdd(string):
    return string[::2]

input_string = "example"
result = removeOdd(input_string)
print(result)
