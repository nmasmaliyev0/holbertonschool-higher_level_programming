#!/usr/bin/python3
"""This module provides basic understanding of input-output."""


def write_file(filename="", text=""):
    """This function writes the given text to the given file"""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)

        return len(text)
