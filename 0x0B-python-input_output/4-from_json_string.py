#!/usr/bin/python3
""" from_json_string module """
import json


def from_json_string(my_str):
    """
        function to load a json from a string
        Args:
            my_str: string
    """
    return json.loads(my_str)
