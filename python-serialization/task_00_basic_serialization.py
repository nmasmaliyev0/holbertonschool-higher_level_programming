#!/usr/bin/python3
import json


def serialize_and_save_to_file(data, filename):
    with open(filename, "w", encoding="utf-8") as file:
        json_str = json.dumps(data)
        file.write(json_str)


def load_and_deserialize(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
