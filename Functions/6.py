#Write a Python function to check whether a number falls in a given range.
def check_range(num, low, high):
    if num >= low and num <= high:
        return num
    else:
        return "Invalid input"
print(check_range(4, 1, 20))