"""
Problem 5: Write a function to compute the total number of lines of code in all
python files in the specified directory recursively.
"""


import os
def find(dir):
    f = os.listdir(dir)
    list4 = []
    for i in f:
        if '.py' in i:
            list4.append(i)

    for j in list4:
        file = open(os.path.join(dir, j)).readlines()

        print(j, len(file))


print(find('chapter 5'))