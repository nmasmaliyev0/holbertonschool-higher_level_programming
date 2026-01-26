#!/usr/bin/python3
"""This module introduces basic Python class structure, private attributes."""


class Square:
    """This class represents a square."""
    def __init__(self, size=0):
        """Initializes a Square instance with a given size after validation"""
        if type(size) is not int:
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
