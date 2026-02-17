#!/usr/bin/python3
"""This module provides basic understanding of json strings"""
import json


def from_json_string(my_str):
    """This function converts json string to dictionary"""
    json_obj = json.loads(my_str)

    return json_obj
