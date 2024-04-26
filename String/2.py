#Write a Python program to count the number of characters (character frequency) in a string.
def charFrequency(string):
    dictionary = {}
    for n in string:
        if n in dictionary:
            dictionary[n] += 1
        else:
            dictionary[n] = 1
    
    return dictionary

print(charFrequency('WSB-Merito')) 