#Write a Python function to create an HTML string with tags around the word(s).
def addHTML(text, tag):
    return f"<{tag}>{text}</{tag}>"

word = "random"
tag = "org"
html_string = addHTML(word, tag)
print(html_string)
