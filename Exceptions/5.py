def open_file_with_permission_check(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return f"File content:\n{content}"
    except PermissionError:
        return f"Error: Permission denied. You do not have the necessary permissions to open the file '{filename}'."
    except FileNotFoundError:
        return f"Error: The file '{filename}' does not exist."

if __name__ == '__main__':
    filename = input("Please enter the file name to open: ")
    print(open_file_with_permission_check(filename))
