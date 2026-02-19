#!/usr/bin/python3
def class_to_json(obj):
    """This function turns a class instance into a dictionary"""
    return obj.__dict__
