#Write a Python function to check whether a string is a pangram or not.
import string
def is_pangram(s):
    return set(string.ascii_lowercase).issubset(set(s.lower()))

print(is_pangram("There once was a ship"))