"""
Problem 9: Write a function permute to compute all possible permutations of elements of a given list.
"""

import itertools
def permute(new_list):
    xx=itertools.permutations(new_list)
    print(list(xx))

permute([1,2,3])