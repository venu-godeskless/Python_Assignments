"""
Problem 27: Write a function triplets that takes a number n as argument and
returns a list of triplets such that sum of first two elements of the triplet equals the third element using numbers below n.
Please note that (a, b, c) and (b, a, c) represent same triplet.
"""
from reportlab.lib.utils import flatten


def triplets(n):
    """1st method"""
    for i in range(1,n):
        for j in range(i,n):
            for z in range(j,n):
                if i+j==z:
                    x=[i,j,z]
                    print(x)

    """2nd method"""
    print([(i,j,z)for i in range(1,n) for j in range(i,n) for z in range(j,n) if i+j==z])
triplets(5)
