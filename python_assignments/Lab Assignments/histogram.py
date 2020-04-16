"""
Define a procedure histogram() that takes a list of integers and prints a histogram to
the screen. For
example, histogram([4, 9, 7]) should print the following:
****
*********
*******
"""

#HISTOGRAM USING SPLITTING STRING AND CONVERTED INTO LIST

str= input("enter a string: ")
new_str = str.split(",")
# print(new_str)--after splitting

for i in new_str:
    c=''
    t=int(i)
    while t>0:
        c+='*'
        t-=1
    print(c)


# # HISTOGRAM USING ARRAY AS A INPUT

# from array import *
# arr = array('i',[])
#
# n= int(input("enter the elements"))
# # arr = array('i',[n])
# for i in range(n):
#     data= int(input("enter the values"))
#     arr.append(data)
# # print(arr)
# for j in arr:
#     s=''
#     t=j
#     while (t>0):
#         s+='*'
#         t-=1
#
#     print(s)


# HISTOGRAM USING TAKING ONE BY ONE ELEMENTS AND STORE

# a= int(input("enter size of a list':"))
# l=[]
# for i in range(a):
#     j=int(input())
#     l.append(j)
# # print(l)
# for i in l:
#     s=''
#     t=i
#     while(t>0):
#         s+='*'
#         t-=1
#     print(s)


#HISTOGRAM USING FUNCTION

# def hist(n):
#     # x=[]
#     for i in n:
#         # x=[]
#         x = ''
#         y = i
#         while (y > 0):
#             x += '*'
#             y -= 1
#         print(x)
# #
# #
# # #
# hist([2, 3, 4])