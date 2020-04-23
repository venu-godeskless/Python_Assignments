"""
Problem 2.11: Write a function dups to find all duplicates in the list.
"""

def dup(lis):
    new_dup=set(lis)
    return list(new_dup)

print(dup([1,2,3,2,7,1,5,6,5,5,5,7,7,10]))
