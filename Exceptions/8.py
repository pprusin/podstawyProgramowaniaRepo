def divide_numbers(numerator, denominator):
    try:
        result = numerator / denominator
        return f"The result of dividing {numerator} by {denominator} is {result}."
    except ArithmeticError as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    try:
        numerator = float(input("Please enter the numerator: "))
        denominator = float(input("Please enter the denominator: "))
        print(divide_numbers(numerator, denominator))
    except ValueError:
        print("Error: Please enter valid numbers.")
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
