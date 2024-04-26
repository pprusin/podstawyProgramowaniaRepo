#Write a Python program to calculate the length of a string.
def stringLength(string):
    count = 0
    for char in string:
        count += 1
    return count

print('String length is :', stringLength('sampleString'))
