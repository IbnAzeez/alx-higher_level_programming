#!/usr/bin/python3
""" text_indentation module """


def text_indentation(text):
    """ text_indentation function
    this function split a text by punctuation
    Attributes:
        text: text to split
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()
    text = text.replace(".", ".\n")
    text = text.replace("?", "?\n")
    text = text.replace(":", ":\n")
    text = text.rstrip()

    if len(text) == 0:
        return

    for key, line in enumerate(list(text.split("\n"))):
        line = line.strip()
        print("{}".format(line))
        if key < len(list(text.split("\n"))) - 1:
            print()
