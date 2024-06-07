#!/usr/bin/python3
"""
The following function simulates the process of opening boxes
starting from the first box (index 0). Each box contains
keys to other boxes. The objectif is to determine if all boxes
can eventually be opened using the available keys.
"""


def canUnlockAll(boxes):
    """
    checks if all the boxes can be opened

    Args:
        boxes (list of list of int): A list where each element is a list of
        keyscontained in the corresponding box.
    """
    keys = [0]
    for key in keys:
        for myKey in boxes[key]:
            if myKey not in keys and myKey < len(boxes):
                keys.append(myKey)
    if len(keys) == len(boxes):
        return True
    return False
