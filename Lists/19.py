#Write a Python program to check whether two lists are circularly identical.
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 1, 2]
isCircular = ''.join(map(str, list1)) in ''.join(map(str, list2 * 2))
print(isCircular)
