"""
Problem 2.14: Improve the unique function written in previous problems to take an optional
key function as argument and use the return value of the key function to check for uniqueness.
"""


def un(li):

    ##--1st method--
    new_str=set(li)
    return list(new_str)

    ##2nd--method--
    n=[]
    l=[]
    for i in li:
        if i not in n:
            l.append(i)
            n.append(i)
    return n


x1=un(['venu','ratan','venu','ratan'])
print(x1)