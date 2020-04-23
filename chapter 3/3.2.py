"""
Problem 2: Write a program extcount.py to count number of files for each extension in the given directory.
The program should take a directory name as argument and print count and extension for each available file extension.
"""
from collections import Counter
import os

def direct(dir):
    f=os.listdir(dir)
    l=[]
    for i in f:
        l.append(i.split('.')[-1])


    my_dict = {i: l.count(i) for i in l}
    print(my_dict)

    c=Counter(l)
    print(c)

direct('chapter 2')