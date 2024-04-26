#Write a Python program to remove duplicates from a list.
def remove_duplicates(items):
    return list(set(items))

print(remove_duplicates([1,2,3,1,2,4,5]))
