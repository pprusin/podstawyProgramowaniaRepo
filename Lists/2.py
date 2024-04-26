#Write a Python program to multiply all the items in a list.
def multiplyList(items):
    ammount = 1
    for x in items:
        ammount *= x
    return ammount

print(multiplyList([1, 2, 3, 4]))
