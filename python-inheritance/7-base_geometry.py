#!/usr/bin/python3
"""Provides a basic class"""


class BaseGeometry:
    """Defines a base geometry"""
    def area(self):
        """Raises Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates name, raises exception if condition fails"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".fornat(name))
