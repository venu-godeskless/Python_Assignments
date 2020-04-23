"""
Problem 9: The built-in function enumerate takes an iteratable and
returns an iterator over pairs (index, value) for each value in the source.
"""

def my_enumrate(list):
    for i,j in enumerate(list):
        print(i,j)

my_enumrate(['a','b','c','d'])