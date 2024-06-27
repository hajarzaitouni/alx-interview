#!/usr/bin/python3
""" UTF-8 Validation """

from typing import List


def validUTF8(data: List[int]) -> bool:
    """ Check if data represents a valid UTF-8 encoding. """
    n_bytes = 0

    for i in data:
        i = i & 0xFF  # 10010110 & 11111111 results in 10010110 (which is 150)

        if n_bytes > 0:
            if (i >> 6) != 2:
                return False
            n_bytes -= 1
        else:
            if (i >> 7) == 0:
                n_bytes = 0
            elif (i >> 5) == 6:
                n_bytes = 1
            elif (i >> 4) == 14:
                n_bytes = 2
            elif (i >> 3) == 30:
                n_bytes = 3
            else:
                return False
    # If n_bytes is not zero, it means there are trailing bytes missing
    return n_bytes == 0
