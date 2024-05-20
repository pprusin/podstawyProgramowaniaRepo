#Write a Python program to count the number of even and odd numbers from a series of numbers.
def count_even_odd(lst):
    even = sum(1 for num in lst if num % 2 == 0)
    odd = sum(1 for num in lst if num % 2 != 0)
    return even, odd

list = [2, 23, 43, 1, 12]
print(count_even_odd(list))