# Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.
def changeFirstwithLast(string):
    if len(string) <= 1:
        return string
    else:
        return string[-1] + string[1:-1] + string[0]

inputString = "sample"
result = changeFirstwithLast(inputString)
print(result)
