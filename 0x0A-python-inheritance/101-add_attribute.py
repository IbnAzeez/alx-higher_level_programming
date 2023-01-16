#!/usr/bin/python3
""" add_attribute module """


def add_attribute(obj, name, value):
    """ add_attribute function """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    if (not hasattr(obj, name)):
        prmObject.__setattr__(name, value)
