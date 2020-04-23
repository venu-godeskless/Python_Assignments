"""
Problem 38: Write a function invertdict to interchange keys and values in a dictionary.
For simplicity, assume that all values are unique.
"""


def invertdict(dict):
    """1st method"""
    new_dict={}
    for i,j in dict.items():
        new_dict[j]=i

    print(new_dict)


    """2nd method"""
    print({j:i for i,j in dict.items()})

invertdict({'x': 1, 'y': 2, 'z': 3})