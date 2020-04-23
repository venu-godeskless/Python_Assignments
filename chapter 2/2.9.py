"""
Problem 2.9: Write a function cumulative_product to compute cumulative product of a list of numbers.
"""

##---method 1---
import numpy as np
print(np.cumprod([1,2,3,4]))


##---method 2---
def prod(lis):
    x=1
    for i in lis:
        x*=i
        yield x


print(list(prod([1,2,3,4])))