# Write a Python function that takes a list of words and return the longest word and the length of the longest one.
def theLongestWord(words):
    longest = words[0]
    longestLength = len(longest)

    for word in words[1:]:
        if len(word) > longestLength:
            longest = word
            longestLength = len(word)

    return longest, longestLength

word_list = ['apple', 'banana', 'orange', 'strawberry']
theLongestWord, length = theLongestWord(word_list)
print("Longest word:", theLongestWord)
print("Length of the longest word:", length)
