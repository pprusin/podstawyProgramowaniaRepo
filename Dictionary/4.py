# Write a Python script to check whether a given key already exists in a dictionary.
def checkKEy(d, key):
    return key in d

sample_dict = {'a': 1, 'b': 2, 'c': 3}
key_to_check = 'b'

if checkKEy(sample_dict, key_to_check):
    print(f"The key '{key_to_check}' exists in the dictionary.")
else:
    print(f"The key '{key_to_check}' does not exist in the dictionary.")
