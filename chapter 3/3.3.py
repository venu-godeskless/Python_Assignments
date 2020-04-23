"""
Problem 3.3:
Write a program to list all the files in the given directory along with their length and last modification time.
The output should contain one line for each file containing filename, length and modification date separated by tabs.
"""


import os.path, time

def directories(dir):
    f=os.listdir(dir)
    dirr=[]
    for i in f:
        dirr.append(i)

    for j in dirr:
        files=open(os.path.join(dir,j)).readlines
        print("This is file={},this is length of file={}".format(j,len(files)))

directories('chapter 5')
