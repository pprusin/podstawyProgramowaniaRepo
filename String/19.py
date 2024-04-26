#Write a Python program to display a number with a comma separator.
def commaSep(number):
    return "{:,}".format(number)

number = 1000000
formatted_number = commaSep(number)
print("Number with comma separator:", formatted_number)
