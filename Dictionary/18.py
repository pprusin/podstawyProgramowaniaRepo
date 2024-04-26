#Write a Python program to replace dictionary values with their sums.
def replaceWithSum(d):
    for key, value in d.items():
        if isinstance(value, list):
            d[key] = sum(value)
    return d

sample_dict = {'a': [1, 2, 3], 'b': 2, 'c': [4, 5], 'd': 'string'}

changedDict = replaceWithSum(sample_dict)
print("Modified Dictionary with sums:")
print(changedDict)
