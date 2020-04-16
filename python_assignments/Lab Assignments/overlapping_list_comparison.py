# """
# Define a function overlapping() that takes two lists and returns True if they have
# at least one
# member in common, False otherwise
# """
#
#
def overlapping(lis1,lis2):
    # print(lis1)--printing list1
    # print(lis2)--printing list 2

    """1st method"""

    # for i in lis1:
    #     if i not in lis2:
    #         pass
    #     else:
    #         return True

    """2nd method"""
    # for i in lis1:
    #     for j in lis2:
    #         if i==j:
    #             return True
    #         else:
    #             pass

    """3rd method"""
    return [True for i in lis1 for j in lis2 if i==j ]


# x=overlapping([2,3,5],[8,0,7])
x=overlapping([2,3,5],[5,9,7])
# print(x)

# if x==None:
#     print(False)
# else:
#     print(True)

# print(False) if x==None else print(True)

# if x==[]:
#     print(False)
# else:
#     print(True)


##using ternary operator--
print(False) if x==[] else print(True)