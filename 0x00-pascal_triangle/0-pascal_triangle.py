#!/usr/bin/python3
""" create a module for Pascal's Triangle Function """


def pascal_triangle(n):
    """ returns a list of lists of ints
        representing the Pascal's triangle of n
    """
    if n <= 0:
        return []

    result = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(result[i-1][j-1] + result[i-1][j])
        row.append(1)
        result.append(row)

    return result
