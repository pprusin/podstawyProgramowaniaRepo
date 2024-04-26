#Write a Python program to check if multiple keys exist in a dictionary.
def checkIFkeyExist(d, keys):
    return all(key in d for key in keys)

dictionary = {'a': 1, 'b': 2, 'c': 3}

keys_to_check = ['a', 'b', 'd']

if checkIFkeyExist(dictionary, keys_to_check):
    print("All keys exist in the dictionary.")
else:
    print("Not all keys exist in the dictionary.")
