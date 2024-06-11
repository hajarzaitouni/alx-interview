#!/usr/bin/python3
"""
Implement a function that calculate the min number of operations needed
to achieve exactly n H characters in a file using Copy All and Paste operations
"""


def minOperations(n: int) -> int:
    """
    Calculate the fewest number of operations needed to result
    in exactly n H characters in the file.

    n: Target number of H characters
    """
    if n <= 1:
        return 0

    count_operations = 0
    divisor = 2

    while (n > 1):
        while n % divisor == 0:
            count_operations += divisor
            n //= divisor
        divisor += 1

    return count_operations
