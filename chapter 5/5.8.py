"""
Problem 8: Write a function peep, that takes an iterator as argument and
returns the first element and an equivalant iterator.
"""

def peep(n):
    a=list(n)
    return a[0],list(a)
print(peep(range(5)))