#Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
def case_count(s):
    upper = sum(1 for char in s if char.isupper())
    lower = sum(1 for char in s if char.islower())
    return upper, lower

print(case_count("SzczebrzeszyN"))