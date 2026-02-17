#!/usr/bin/python3
"""This module provides basic understanding of input-output."""


def append_write(filename="", text=""):
    """This function appends the given text to the given file"""
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)

        return len(text)
