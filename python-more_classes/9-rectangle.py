#!/usr/bin/python3
"""This module introduces basic Python class structure and syntax."""


class Rectangle:
    """This class represents a rectangle."""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """This method is for initializing an instance of the class"""
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

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

    def __str__(self):
        if self.__height * self.__width == 0:
            return ""

        lines = []
        for _ in range(self.__height):
            lines.append(str(self.print_symbol) * self.__width)

        return "\n".join(lines)

    def __repr__(self):
        """This return string representation of the rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """A special class method that mounts when a class is deleted"""
        print("Bye rectangle...")

        self.__class__.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1

        return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
