#Write a Python program to get the total length of all values in a given dictionary with string values.
def totalLength(d):
    length = sum(len(value) for value in d.values() if isinstance(value, str))
    return length

original_dict = {'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}

length = totalLength(original_dict)
print("Total length of all values of the dictionary with string values:", length)
