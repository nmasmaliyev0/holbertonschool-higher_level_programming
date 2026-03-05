#!/usr/bin/python3
"""Provides a basic class"""


class BaseGeometry:
    """Defines a base geomerty"""
    def area(self):
        raise Exception("area() is not implemented")
