"""
Problem 2.13: Write a function lensort to sort a list of strings based on length.
"""
def lensort(list):

    new_str=sorted(list,key=len)
    return new_str



x=lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby'])
print(x)