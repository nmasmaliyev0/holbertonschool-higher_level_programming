#!/usr/bin/python3
"""This module introduces basic Python class structure, private attributes."""


class Square:
    """This class represents a square."""
    def __init__(self, size=0, position=(0, 0)):
        """Initialiing a Square instance object with a given size"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Using Getter for retrieving size"""
        return self.__size

    @property
    def position(self):
        """Using Getter for retrieving position"""
        return self.__position

    @size.setter
    def size(self, size):
        """Using Setter to accept value for the __size by validation"""
        if type(size) is not int:
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @position.setter
    def position(self, position):
        """Using Setter to accept value for the __position by validation"""
        if (
            type(position) is not tuple or
            len(position) != 2 or
            type(position[0]) is not int or
            type(position[1]) is not int or
            position[0] < 0 or
            position[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")

        else:
            self.__position = position

    def area(self):
        """Creates a public instance method that return area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Creates a public method that prints square based on its size and puts spaces"""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0], "#" * self.__size)
