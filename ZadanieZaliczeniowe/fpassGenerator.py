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
    print("Generator Bezpiecznych Haseł")
    
    try:
        num_passwords = int(input("Ile haseł chcesz wygenerować? "))
        length = int(input("Jak długie ma być każde hasło? (minimum 12) "))
        include_special_chars = input("Czy chcesz uwzględnić znaki specjalne? (tak/nie) ").strip().lower() == 'tak'
        
        if length < 12:
            print("Długość hasła musi wynosić przynajmniej 12 znaków.")
            return

        print("\nWygenerowane Hasła:")
        for i in range(num_passwords):
            password = generate_password(length, include_special_chars)
            print(f"{i + 1}. {password}")

    except ValueError:
        print("Wprowadzono nieprawidłowe dane. Proszę wprowadzić poprawne liczby.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

if __name__ == "__main__":
    main()
