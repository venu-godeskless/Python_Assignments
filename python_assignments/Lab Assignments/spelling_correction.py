"""
Define a simple "spelling correction" function correct() that takes a string and
sees to it that
1) two or more occurrences of the space character is compressed into one, and
2) inserts an extra space after a period if the period is directly followed by a letter.
e.g. correct("This is very funny and cool.Indeed!") should return "This is very funny
and cool. Indeed!"
"""

##1--
def correct(str):

    return " ".join(str.split())

x='    this         is very good'
# print(correct(x))

##2--

import re

def correction(s):
    res = re.sub('\s+$', '', re.sub('\s+', ' ', re.sub('\.', '. ', s)))
    if res[-1] != '.':
       res += '.'
    return res

s="This is very funny and cool.Indeed!"
print(correction(s))