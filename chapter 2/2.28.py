"""
Problem 28: Write a function enumerate that takes a list and
returns a list of tuples containing (index,item) for each item in the list.
"""

def enum(list):
    """1st method"""
    for i,j in enumerate(list):
        print(i,j)

    """2nd method"""
    print([(i,j) for i,j in enumerate(list)])

enum(['a','b','c','d','e'])