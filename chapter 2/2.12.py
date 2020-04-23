"""
Problem 2.12: Write a function group(list, size) that take a list and splits into smaller lists of given size.
"""

def group(list,size):

    for i in range(0, len(list), size):
        yield list[i:i + size]

print(list(group([1,2,3,5,7,8,6,788,9,0],3)))