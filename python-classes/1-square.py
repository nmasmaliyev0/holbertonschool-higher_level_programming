#!/usr/bin/python3
"""This module introduces basic Python class structure, private attributes."""


class Square:
    """This class represents a square."""
    def __init__(self, size):
        """Initializes a Square instance with a given size."""
        self.__size = size
