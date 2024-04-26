#Write a Python script to concatenate the following dictionaries to create a new one.
def concatDicts(*dicts):
    concatenatedDict = {}
    for d in dicts:
        concatenatedDict.update(d)
    return concatenatedDict

dict1 = {1: 'a', 2: 'b'}
dict2 = {3: 'c', 4: 'd'}
dict3 = {5: 'e', 6: 'f'}

concatenatedDict = concatDicts(dict1, dict2, dict3)
print("Concatenated Dictionary:", concatenatedDict)
