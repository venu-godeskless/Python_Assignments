"""
Problem 25: Python provides a built-in function map that applies a function to each element of a list.
Provide an implementation for map using list comprehensions.
"""


def square(n):
    return n*n


n1=[i for i in range(10)]
print(list(map(square,n1)))