#Write a Python program to check if a dictionary is empty or not.
def isEmpty(d):
    return not bool(d)

dictionary = {}
print("Is the dictionary empty?", isEmpty(dictionary))

dictionary = {'a': 1, 'b': 2}
print("Is the dictionary empty?", isEmpty(dictionary))
