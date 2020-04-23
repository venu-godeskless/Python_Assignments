"""
Problem 26: Python provides a built-in function filter(f, a) that returns items of the list a for which f(item) returns true.
Provide an implementation for filter using list comprehensions.
"""


def even(n):
    if n%2==0:
        return n


n2=[i for i in range(10)]
print(list(filter(even,n2)))