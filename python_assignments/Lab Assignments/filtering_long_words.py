"""
Write a function filter_long_words() that takes a list of words and an integer n
and returns the list of
words that are longer than n
"""

def filter_long_words(list,n):
    # new_list=[]
    # for i in list:
    #     if len(i)>=n:
    #         new_list.append(i)
    #     else:
    #         pass

    new_list=[i for i in list if len(i)>=n ]
    return new_list


x=filter_long_words(['venu','ratan','mayuri'],5)
print(x)

