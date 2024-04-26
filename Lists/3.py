#Write a Python program to get the largest number from a list.
def largestNum(list):
    for i in list:
        largestNum = max(list) 
        return largestNum
    
print(largestNum([1,7,6,8,19]))