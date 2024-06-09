#!/usr/bin/env python3
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to JSON and save it to a file.

    :param data: A Python dictionary with data
    :param filename: The filename of the output JSON file
    """
    with open(filename, 'w') as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """
    Load and deserialize data from a JSON file.

    :param filename: The filename of the input JSON file
    :return: A Python dictionary with the deserialized data
    """
    with open(filename, 'r') as f:
        data = json.load(f)
        return data
