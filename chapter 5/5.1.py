"""
Problem 1: Write an iterator class reverse_iter, that takes a list and iterates it from the reverse direction. ::
"""

class reverse_iter:
    def __init__(self,l):
        self.index=len(l)
        # print(self.index)
        self.data=l
        # print(self.data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index==0:
            raise StopIteration
        self.index=self.index-1
        return self.data[self.index]


for i in reverse_iter([1,2,3,4,5]):
    print(i)