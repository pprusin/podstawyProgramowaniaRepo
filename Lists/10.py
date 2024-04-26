#Write a Python program to find the list of words that are longer than n from a given list of words.
def longWordFiltered(words, n):
    return [word for word in words if len(word) > n]

print(longWordFiltered(['hello', 'world', 'hi', 'name'], 3))
