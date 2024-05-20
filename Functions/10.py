#Write a Python function to print the even numbers from a given list.
def even_numbers(lst):
    return [num for num in lst if num % 2 == 0]

x = [1, 4, 1566]
print(even_numbers(x))