#Write a Python program to remove a newline in Python
def rmvNewLine(text):
    return text.replace('\n', '')

input_text = "Hello\nWorld\n"
result = rmvNewLine(input_text)
print("String after removing newlines:", result)
