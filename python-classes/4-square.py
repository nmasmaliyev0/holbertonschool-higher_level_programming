#!/usr/bin/python3
"""This module introduces basic Python class structure, private attributes."""


class Square:
    """This class represents a square."""
    def __init__(self, size=0):
        """Initialiing a Square instance object with a given size"""
        self.size = size

    @property
    def size(self):
        """Using Getter for retrieving size"""
        return self.__size

    @size.setter
    def size(self, size):
        """Using Setter to accept value for the __size by validation"""
        if type(size) is not int:
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Creates a public instance method that return area of the square"""
        return self.__size ** 2
