def get_number_input(prompt):
    user_input = input(prompt)
    try:
        value = float(user_input)
        return value
    except ValueError:
        raise TypeError(f"Invalid input: {user_input}. You must enter a valid number.")

if __name__ == '__main__':
    try:
        number1 = get_number_input("Please enter the first number: ")
        number2 = get_number_input("Please enter the second number: ")
        print(f"The numbers you entered are {number1} and {number2}.")
    except TypeError as e:
        print(e)
