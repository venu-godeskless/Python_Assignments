"""
Problem 37: Write a function valuesort to sort values of a dictionary based on the key.
"""


def valuesort(dict):

    """"1st method"""
    c=[]
    for key,value in sorted(dict.items()):
        c.append(value)
    return c

    """using list comprehension"""
    return [j for i,j in sorted(dict.items())]

print(valuesort({'x': 1, 'y': 2, 'a': 3}))