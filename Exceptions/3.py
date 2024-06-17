def open_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return f"File content:\n{content}"
    except FileNotFoundError:
        return f"Error: The file '{filename}' does not exist."

if __name__ == '__main__':
    filename = input("Please enter the file name to open: ")
    print(open_file(filename))
