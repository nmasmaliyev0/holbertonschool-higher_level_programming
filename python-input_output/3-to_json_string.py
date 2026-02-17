#!/usr/bin/python3
"""This module provides basic understanding of json strings"""
import json


def to_json_string(my_obj):
    """This function takes an object and turns it into a json string"""
    json_string = json.dumps(my_obj)

    return json_string
