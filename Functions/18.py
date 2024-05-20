#Write a Python function to concatenate all elements in a list into a string and return it.
def concatenate_list(lst):
    return ''.join(map(str, lst))

list = ['bomb', 21, "BOOOOM!"]
print(concatenate_list(list))