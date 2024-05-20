#Write a Python function that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
def sort_hyphenated(s):
    words = s.split('-')
    words.sort()
    return '-'.join(words)

print(sort_hyphenated("There-once-was-a-ship"))