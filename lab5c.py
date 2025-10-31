#!/usr/bin/env python3
# Author: Sashank Kharal

def add(number1, number2):
    """
    Adds two numbers together.
    Returns the result.
    If an exception occurs returns 'error: could not add numbers'
    """
    try:
        return int(number1) + int(number2)
    except (ValueError, TypeError):
        return 'error: could not add numbers'


def read_file(filename):
    """
    Reads a file and returns a list of all lines (including newline characters).
    If file cannot be read, returns 'error: could not read file'
    """
    try:
        with open(filename, 'r') as f:
            return f.readlines()
    except (FileNotFoundError, PermissionError, IsADirectoryError, OSError):
        return 'error: could not read file'


if __name__ == '__main__':
    # Test the add() function
    print(add(10, 5))         # works
    print(add('10', 5))       # works
    print(add('abc', 5))      # exception

 # Test the read_file() function
    print(read_file('seneca2.txt'))    # works if file exists
    print(read_file('file10000.txt'))  # exception file doesn't exist
