#Write a Python program to iterate over dictionaries using for loops.
ditionary = {'a': 1, 'b': 2, 'c': 3}

print("Iterating over keys:")
for key in ditionary:
    print(key)

print("\nIterating over values:")
for value in ditionary.values():
    print(value)

print("\nIterating over key-value pairs:")
for key, value in ditionary.items():
    print(key, "->", value)
