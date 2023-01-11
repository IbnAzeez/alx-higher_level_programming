#!/usr/bin/python3
""" write_file module """


def write_file(prmFileName="", prmText=""):
    """
        function that write a specific text in a specific file
        Args:
            prmFileName: name of the file
            prmText: text to write
    """
    character = 0
    with open(prmFileName, 'w', encoding="UTF-8") as file:
        character = file.write(prmText)
    file.closed
    return character
