"""
Problem 2.16: Write a function extsort to sort a list of files based on extension.
"""

import os
v=['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c']
v.sort(key=lambda f:os.path.splitext(f)[1])
print(v)

def extsort(str):

    n=list(str)
    n.sort(key=lambda new:os.path.splitext(new)[1])
    return n

x2=extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])
print(x2)