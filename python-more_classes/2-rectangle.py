#!/usr/bin/python3
"""This module introduces basic Python class structure and syntax."""


class Rectangle:
    """This class represents a rectangle."""
    def __init__(self, width=0, height=0):
        """This method is for initializing an instance of the class"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Using Getter for retrieving width"""
        return self.__width

    @property
    def height(self):
        """Using Getter for retrieving height"""
        return self.__height

    @width.setter
    def width(self, value):
        """Using Setter to accept a new value for __width by validation"""
        if type(value) is not int:
            raise TypeError('width must be an integer')

        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @height.setter
    def height(self, value):
        """Using Setter to accept a new value for __height by validation"""
        if type(value) is not int:
            raise TypeError('height must be an integer')

        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

    def area(self):
        """A public instance method for computing the area of a rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """A public instance method for computing perimeter of a rectangle"""
        if self.__height * self.__width == 0:
            return 0

        return 2 * (self.__height + self.__width)
