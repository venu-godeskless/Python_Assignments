"""
Problem 29: Write a function array to create an 2-dimensional array.
The function should take both dimensions as arguments. Value of each element can be initialized to None:
"""
def str(n1,n2):

    return [[None]*n2 for i in range(1,n2)]


a=str(2,3)
a[0][0]=5
print(a)