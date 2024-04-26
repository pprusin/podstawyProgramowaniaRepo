#Write a Python program to count the occurrences of each word in a given sentence.
def countOccurencies(sentence):
    word_counts = {}
    words = sentence.split()

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts

input_sentence = "Jestem przykladowym zdaniem"
word_occurrences = countOccurencies(input_sentence)
print("Word occurrences:", word_occurrences)
