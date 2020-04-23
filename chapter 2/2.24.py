"""
Problem 24: Provide an implementation for zip function using list comprehensions.
"""


"""---1st-method---"""

def str(*list):
    return range(len(sorted(list,key=len)[0]))

alpha=['a','b','c']
nos=[1,2,3]
g=((nos[i],alpha[i])for i in str(nos,alpha))
for item in g:
    print(item)



"""--2nd-method---"""
def string(*list):
    for i,j in zip(*list):
        print(i,j)

alpha=['a','b','c']
nos=[1,2,3]
string([1,2,3,4],['a','b','c','d'])