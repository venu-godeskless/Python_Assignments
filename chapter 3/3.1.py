"""
Problem 1: Write a program to list all files in the given directory.
"""
import os
def directory(dir):
    f=os.listdir(dir)
    for i in f:
        print(i)


directory('chapter 5')