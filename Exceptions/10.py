def perform_list_operation(lst, operation):
    try:
        result = getattr(lst, operation)()
        return f"Result of '{operation}': {result}"
    except AttributeError:
        return f"Error: The list object does not have a '{operation}' method."

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(f"Sample list: {sample_list}")
    
    operation = input("Please enter the list operation to perform (e.g., 'append', 'pop', 'non_existent_method'): ")
    if operation in ['append', 'insert']:
        print("Note: For 'append' and 'insert' operations, a value will be added to the list.")
        if operation == 'append':
            sample_list.append('new_value')
        elif operation == 'insert':
            sample_list.insert(0, 'new_value')
    else:
        print(perform_list_operation(sample_list, operation))
    
    print(f"Updated list: {sample_list}")
