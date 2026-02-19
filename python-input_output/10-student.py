#!/usr/bin/python3
"""This module shows a way to turn class instances to dicts by filtering"""


class Student:
    """This class defines a new Student"""
    def __init__(self, first_name, last_name, age):
        """Intialize a new Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dict represantation of Student based on given keys"""
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            new_dict = {}

            for attr in attrs:
                if attr in self.__dict__:
                    new_dict[attr] = self.__dict__[attr]

            return new_dict

        return self.__dict__
