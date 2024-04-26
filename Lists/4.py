#Write a Python program to get the smallest number from a list.
def smallestNumber(list):
    for i in list:
        smallestNum = min(list) 
        return smallestNum
    
print(smallestNumber([1,7,6,8,19]))