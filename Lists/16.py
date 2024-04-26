#Write a Python program to flatten a shallow list.
shallowList = [[1, 2], [3, 4], [5, 6]]
flattenedList = [item for sublist in shallowList for item in sublist]
print(flattenedList)
