"""Problem 1: What will be the output of the following program?"""

from math import factorial

x = [0, 1, [2]]
x[2][0] = 3
print(x)  ##will append values in second list with given index
x[2].append(4)
print(x) #---- will append values in second list
x[2] = 2
print(x) #---will replace the given index with value





"""
Problem 2.3:What happens when the above sum function is called with a list of strings?
Can you make your sum function work for a list of strings as well.
"""

print(sum(["venu","maduta"]))



"""
Problem 2.4: Implement a function product, to compute product of a list of numbers.
"""
from math import prod
print(prod([1,2,4,5]))



"""
Problem 2.5: Write a function factorial to compute factorial of a number.
Can you use the product function defined in the previous example to compute factorial?
"""

print(factorial(4))
print(factorial(10))


"""
Problem 2.6: Write a function reverse to reverse a list. Can you do this without using list slicing?
"""

print(reversed([1,2,3,5]))

li=[1,2,3,5]
li.reverse()
print(li)



"""
Problem 2.7: Python has built-in functions min and max to compute minimum and maximum of a given list. 
Provide an implementation for these functions. 
What happens when you call your min and max functions with a list of strings?
"""

print(max([1,2,3,54,5]))
print(min([1,2,3,54,5,0]))
