#!/usr/bin/python3
"""This module provides a way to turn class instances into dicts"""


def class_to_json(obj):
    """This function turns a class instance into a dictionary"""
    return obj.__dict__
