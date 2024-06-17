def get_integer_input():
    user_input = input("Please enter an integer: ")
    try:
        value = int(user_input)
        return f"You entered the integer: {value}"
    except ValueError:
        raise ValueError("Invalid input. You must enter a valid integer.")

if __name__ == '__main__':
    try:
        print(get_integer_input())
    except ValueError as e:
        print(e)
