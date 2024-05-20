#Write a Python function to create a simple histogram from a given list of integers.
def histogram(lst):
    for num in lst:
        print('*' * num)

list = [1, 10, 2, 1]
print(histogram(list))