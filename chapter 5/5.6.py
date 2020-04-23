"""
Problem 6: Write a function to compute the total number of lines of code,
ignoring empty and comment lines, in all python files in the specified directory recursively.
"""

import os
def find_number_lines(dir):
    f=os.listdir(dir)
    list=[]
    for i in f:
        if '.py' in i:
               list.append(i)
    for j in list:
        file=open(os.path.join(dir,j)).readlines()
        cc=0
        x3='#'
        for x in file:
            if x3 not in x:
                cc+=1
        print(j,cc)
find_number_lines('chapter 2')