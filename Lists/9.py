#Write a Python program to clone or copy a list.
def cloneList(items):
    return items[:]

originalList = [1, 2, 3]
copiedList = cloneList(originalList)
print(copiedList)
