#!/usr/bin/python3
"""
A method that calculates the fewest number of operations
needed to result in exactly n H characters in the file
"""


def minOperations(n):
    """
    calculates the fewest number of operations
    """
    h = 1
    x = 1
    counter = 0

    if n < 2:
        return 0
    while h < n:
        if n % h == 0:
            x = h
            h *= 2
            counter += 2
        else:
            h += x
            counter += 1
    return counter
