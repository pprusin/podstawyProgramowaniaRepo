"""Write a Python program to check the validity of passwords input by users.
Validation :

At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters."""
import re

def is_valid_password(password):
    if len(password) < 6 or len(password) > 16:
        return False
    
    if not re.search("[a-z]", password):
        return False
    
    if not re.search("[A-Z]", password):
        return False
    
    if not re.search("[0-9]", password):
        return False
    
    if not re.search("[$#@]", password):
        return False
    
    return True

passwords = ["Passw0rd", "password123", "Strong#Password", "weakpass", "Good1234#"]
for password in passwords:
    if is_valid_password(password):
        print(f"'{password}' is a valid password.")
    else:
        print(f"'{password}' is not a valid password.")
