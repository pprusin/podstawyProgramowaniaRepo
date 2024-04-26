#Write a Python program that checks whether a string represents an integer or not.
def isInteger(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

print(isInteger("123"))
print(isInteger("12.3"))
print(isInteger("abc"))
print(isInteger("-456"))
