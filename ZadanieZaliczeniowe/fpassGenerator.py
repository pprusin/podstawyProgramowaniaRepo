import string
import secrets

def generate_password(length, use_special_chars):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    if use_special_chars:
        char_pool = letters + digits + special_chars
    else:
        char_pool = letters + digits

    password = ''.join(secrets.choice(char_pool) for _ in range(length))

    return password

def main():
    print("Secure Password Generator")
    
    try:
        num_passwords = int(input("How many passwords do you want to generate? "))
        length = int(input("How long should each password be? (minimum 12) "))
        include_special_chars = input("Do you want to include special characters? (yes/no) ").strip().lower() == 'yes'
        
        if length < 12:
            print("Password length must be at least 12 characters.")
            return

        print("\nGenerated Passwords:")
        for i in range(num_passwords):
            password = generate_password(length, include_special_chars)
            print(f"{i + 1}. {password}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
