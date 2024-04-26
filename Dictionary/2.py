#Write a Python script to add a key to a dictionary.
def addKeytoDict(d, key, value):
    d[key] = value
    return d

sampleDict = {0: 10, 1: 20}
newKey = 2
newKnewValueey = 30

result = addKeytoDict(sampleDict, newKey, newKnewValueey)
print("Expected Result:", result)

