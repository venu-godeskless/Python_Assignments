"""
We can define sum from 1 to x (i.e. 1 + 2 + ... + x) recursively as follows for
integer x ≥ 1:
1, if x = 1
x + sum from 1 to x-1 if x > 1
Complete the following Python program to compute the sum 1 + 2 + 3 + 4 + 5 + 6 + 7
+ 8 + 9 + 10
recursively:
def main():
# compute and print 1 + 2 + ... + 10
print sum(10)
def sum(x):
# you complete this function recursively main()
"""


def sum(n):
    # return n1=n+sum(n-1)

    # if n<=1:
    #     return n
    # else:
    #     return n + sum(n-1)

    return  n if n<=1 else  n+sum(n-1)

# x=5
# print(sum(x))
# res=sum(5)
# print(res)
print(sum(10))