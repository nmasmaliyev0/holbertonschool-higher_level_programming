#!/usr/bin/python3
"""This module provides basic understanding of json strings"""
import json


def load_from_json_file(filename):
    """This function reads a json string inside of a file and turns it to and object"""
    with open(filename) as file:
        json_str = file.read()
        json_obj = json.loads(json_str)

        return json_obj
