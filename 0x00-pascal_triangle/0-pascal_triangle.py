#!/usr/bin/python3
'''Module to return pascal triangle'''


def fat(num):
    '''
    Fatorial
    Args:
        num (int): The number to be factorialed
    Returns:
        The factorial
    '''

    if num == 1 or num == 0:
        return 1
    else:
        return num * fat(num - 1)


def pascal_triangle(num):
    '''
    Pascal's triangle
    Args:
        num (int): The number of rows of the triangle
    Returns:
        List of lists of integers representing the Pascal’s triangle
    '''
    container = []
    if not isinstance(num, int):
        raise TypeError("n must be an integer")
    if num == 0:
        return container
    for x in range(num):
        container.append([])
        for y in range(x+1):
            container[x].append(int(fat(x)/(fat(x-y)*fat(y))))
    return container
