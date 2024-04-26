#Write a Python program to find the highest 3 values of corresponding keys in a dictionary.
def highest_3_values(d):
    sorted_items = sorted(d.items(), key=lambda x: x[1], reverse=True)
    highest_values = sorted_items[:3]
    return highest_values

sample_dict = {'a': 10, 'b': 30, 'c': 20, 'd': 50, 'e': 40}

result = highest_3_values(sample_dict)
print("Highest 3 values of corresponding keys:")
for key, value in result:
    print(f"{key}: {value}")
