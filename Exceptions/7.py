def get_number_input():
    try:
        user_input = input("Please enter a number: ")
        number = float(user_input)
        return f"You entered the number: {number}"
    except ValueError:
        return "Error: The input is not a valid number."
    except KeyboardInterrupt:
        return "\nInput was canceled by the user."

if __name__ == '__main__':
    try:
        print(get_number_input())
    except KeyboardInterrupt:
        print("\nProgram terminated by the user.")
