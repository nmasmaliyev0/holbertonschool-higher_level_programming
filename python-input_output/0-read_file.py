#!/usr/bin/python3
"""This module provides basic understanding of input-output."""


def read_file(filename=""):
    """This function reads and print content of a given file"""
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print(content, end="")
