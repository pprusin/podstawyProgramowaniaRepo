def access_list_element(lst, index):
    try:
        element = lst[index]
        return f"Element at index {index} is {element}."
    except IndexError:
        return f"Error: Index {index} is out of range for the list."

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(f"Sample list: {sample_list}")

    try:
        index = int(input("Please enter the index to access: "))
        print(access_list_element(sample_list, index))
    except ValueError:
        print("Error: You must enter a valid integer.")
