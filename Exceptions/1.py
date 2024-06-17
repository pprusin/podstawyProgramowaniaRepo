def divide_numbers(numerator, denominator):
    try:
        result = numerator / denominator
        return f"The result is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"

# Example usage
if __name__ == '__main__':
    print(divide_numbers(10, 2))   # Expected output: "The result is 5.0"
    print(divide_numbers(10, 0))   # Expected output: "Error: Cannot divide by zero"
