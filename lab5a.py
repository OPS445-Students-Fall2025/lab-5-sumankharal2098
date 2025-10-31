#!/usr/bin/env python3
# Author: Sashank Kharal

def read_file_string(filename):
    """Reads the contents of a file and returns it as a single string"""
    with open(filename, 'r') as f:
        data = f.read()
    return data


def read_file_list(filename):
    """Reads the file and returns a list of lines (without newline characters)"""
    with open(filename, 'r') as f:
        lines = f.readlines()
    return [line.strip() for line in lines]

