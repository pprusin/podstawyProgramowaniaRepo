#Write a Python script to sort (ascending and descending) a dictionary by value.
def sort_dict_by_value(d, ascending=True):
    sorted_dict = dict(sorted(d.items(), key=lambda item: item[1], reverse=not ascending))
    return sorted_dict

example_dict = {'a': 3, 'b': 1, 'c': 2}

sorted_dict_asc = sort_dict_by_value(example_dict)
print(sorted_dict_asc)

sorted_dict_desc = sort_dict_by_value(example_dict, ascending=False)
print(sorted_dict_desc)
