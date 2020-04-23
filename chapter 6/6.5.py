"""
Problem 5: Write a function tree_reverse to reverse elements of a nested-list recursively.
"""


def tree_reverse(li):
    new=[]
    for i in li:
        if isinstance(i,list):
            new.append(tree_reverse(i))
        else:
            new.append(i)
    new.reverse()
    return new

print(tree_reverse([1, 2, [3, 4, [5]]]))