#!/usr/bin/python3
"""
pascal triangle
"""

import sys


def fat(num):
    """
function to return the factorial of num
    """

    if (num == 1 or num == 0):
        return 1
    else:
        return num * fat(num - 1)


def pascal_triangle(num):
    """
pascal triangle na
    """
    container = []
    for x in range(num):
        container.append([])
        for y in range(x+1):
            container[x].append(int(fat(x)/(fat(x-y)*fat(y))))
    return container
