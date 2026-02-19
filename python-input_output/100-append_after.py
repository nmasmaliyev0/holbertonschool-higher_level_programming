#!/usr/bin/python3
"""This module works on adding string after certain string"""


def append_after(filename="", search_string="", new_string=""):
    """Adds new string after given string"""
    with open(filename, "r+") as file:
        lines = file.readlines()

        for i in range(len(lines) - 1, -1, -1):
            if search_string in lines[i]:
                lines.insert(i + 1, new_string)

        file.seek(0)
        file.writelines(lines)
        file.truncate()
