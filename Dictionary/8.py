#Write a Python program to remove duplicates from the dictionary.
def dictNoDuplicates(d):
    dictionary = {}
    for key, value in d.items():
        if value not in dictionary.values():
            dictionary[key] = value
    return dictionary

sampleDict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}

result = dictNoDuplicates(sampleDict)
print("Dictionary after removing duplicates:", result)
