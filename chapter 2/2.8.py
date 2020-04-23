"""
Problem 2.8: Cumulative sum of a list [a, b, c, ...] is defined as [a, a+b, a+b+c, ...].
Write a function cumulative_sum to compute cumulative sum of a list. Does your implementation work for a list of strings?"""

##---method 1---#

import numpy as np
print(np.cumsum([1, 2, 3, 4]))



##---method 2---

def sum(sum):
    x=0
    for i in sum:
        x+=i
        yield x


print(list(sum([1,2,3,5])))