#Write a Python program to sum two integers. However, if the sum is between 15 and 20 it will return 20.
def sum_two(num1, num2):
    if 15<= num1 + num2 <=20:
        return 20
    else:
        return num1 + num2
    
print(sum_two(14,16))
print(sum_two(15,1))