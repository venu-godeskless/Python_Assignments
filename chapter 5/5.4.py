"""
Problem 4: Write a function to compute the number of python files (.py extension) in a specified directory recursively.
"""

import os
def find_py(dir):
    f=os.listdir(dir)
    list=[]
    for i in f:
        # print(i[-3:])
        if i[-3:]=='.py':
            list.append(i)
    return len(list)

print(find_py('chapter 5'))