#!/usr/bin/python3
"""This module provides basic understanding of json strings"""
import json


def save_to_json_file(my_obj, filename):
    """This function turns obj into json string and writes it to a file"""
    with open(filename, "w") as file:
        json_str = json.dumps(my_obj)

        file.write(json_str)
