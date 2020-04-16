"""
Write a function find_longest_word() that takes a list of words and returns the
length of the longest
one.
"""

def find_longest_word(n):
    # x=sorted(n)
    # x=sorted(n,key=len)
    y=sorted(n,key=len,reverse=True)
    return y[0]
    # longest_word=[]
    # for i in n:
    #     for j in i+1:
    #         if len(i)<len(j):
    #             longest_word.append(j)

x=['hiii','venu','ratan']
# print(len(words(x)),x)
print(find_longest_word(x),len(find_longest_word(x)))
# print(words(x))
# print(len(words(x)))