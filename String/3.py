#Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
def stringBothEnds(str):
    if len(str) < 2:
        return ''
    else:
        return str[0:2] + str[-2:]

print(stringBothEnds('przykladoweslowo'))
print(stringBothEnds('12'))
print(stringBothEnds('1'))
