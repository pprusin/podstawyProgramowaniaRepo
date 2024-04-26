#Write a Python program to remove the nth index character from a nonempty string.
def removeChosen(string, n):
    return string[:n] + string[n+1:]

exampleString = "example"
indexToRemove = 2
result = removeChosen(exampleString, indexToRemove)
print("String after removing the character at index", indexToRemove, ":", result)
