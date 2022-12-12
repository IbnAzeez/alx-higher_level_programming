#!/usr/bin/python3
def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    val = list(a_dictionary.keys())[0]
    maximum = a_dictionary[val]
    for key, value in a_dictionary.items():
        if value > maximum:
            maximum = value
            val = key
    return (val)
