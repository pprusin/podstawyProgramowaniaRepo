#Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case).
print("Enter lines (terminate with a blank line):")

lines = []
while True:
    line = input()
    if line:
        lines.append(line.lower())
    else:
        break

print("\nOutput:")
for line in lines:
    print(line)
