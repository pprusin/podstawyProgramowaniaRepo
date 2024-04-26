#Write a Python program that reads two integers representing a month and day and prints the season for that month and day.
month = int(input("Enter the month (as a number): "))
day = int(input("Enter the day (as a number): "))

if (month == 3 and day >= 20) or (month == 4) or (month == 5) or (month == 6 and day < 21):
    season = "Spring"
elif (month == 6 and day >= 21) or (month == 7) or (month == 8) or (month == 9 and day < 23):
    season = "Summer"
elif (month == 9 and day >= 23) or (month == 10) or (month == 11) or (month == 12 and day < 21):
    season = "Autumn"
else:
    season = "Winter"

print("Season:", season)
