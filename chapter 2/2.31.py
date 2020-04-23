"""
Problem 31: Generalize the above implementation of csv parser to support any delimiter and comments.
"""

def filename(filename):
    print([i.split('!') for i in open(filename).readlines() if i[0]!='#'])

filename("new1.txt")