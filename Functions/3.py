#Write a Python function to multiply all the numbers in a list.
def multiply_list(lst):
    result = 1
    for num in lst:
        result *= num
    return result
x = [1, 3, 51, 4123]
print(multiply_list(x))
