#Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
def sortListTuples(tuples):
    return sorted(tuples, key=lambda x: x[-1])

print(sortListTuples([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
