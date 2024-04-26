#Write a Python program to sort a list alphabetically in a dictionary.
def sort_list_in_dict(d):
    sorted_dict = {key: sorted(value) for key, value in d.items()}
    return sorted_dict

sample_dict = {'b': ['banana', 'apple', 'orange'], 'a': ['grape', 'cherry', 'pear']}

sorted_dict = sort_list_in_dict(sample_dict)
print("Dictionary with sorted lists:")
print(sorted_dict)
