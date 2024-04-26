#Write a Python program to get the Fibonacci series between 0 and 50.
a, b = 0, 1
fibbonaciSeries = []

while a <= 50:
    fibbonaciSeries.append(a)
    a, b = b, a + b

print("Fibonacci series between 0 and 50:")
print(fibbonaciSeries)
