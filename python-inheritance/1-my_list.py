#!/usr/bin/python3
"""Defines a MyList class."""


class MyList(list):
    """Inherits from list."""
    def print_sorted(self):
        """Prints the sorted list."""
        print(sorted(self))
