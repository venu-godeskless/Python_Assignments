"""
Problem 2.10: Write a function unique to find all the unique elements of a list.
"""


def unique(lis):
    lis=set(lis)

    return sorted(lis)

print(unique([2,4,6,7,7,8,8,6]))