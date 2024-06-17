def read_file_with_encoding_check(filename, encoding='utf-8'):
    try:
        with open(filename, 'r', encoding=encoding) as file:
            content = file.read()
            return f"File content:\n{content}"
    except UnicodeDecodeError:
        return f"Error: Cannot decode the file '{filename}' with encoding '{encoding}'."
    except FileNotFoundError:
        return f"Error: The file '{filename}' does not exist."
    except PermissionError:
        return f"Error: Permission denied. You do not have the necessary permissions to open the file '{filename}'."

if __name__ == '__main__':
    filename = input("Please enter the file name to open: ")
    encoding = input("Please enter the file encoding (default is 'utf-8'): ") or 'utf-8'
    print(read_file_with_encoding_check(filename, encoding))
