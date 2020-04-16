"""

Object oriented programming
Write a class MyClass it contains 2 members
One number and one string
Write default constructor, parametrized constructor
Overload +,*,- operator
+ - will do the addition of the number and
ascii of 1 st character of the string
‘- - it will chk if num>ascii of 1 st character of the string
Then num-ascii of 1 st character of the string
Else ascii of 1 st character of the string – num
‘* will do the multiplication num and
ascii of last character of the string
"""


class Myclass:

    def __init__(self, str, number):
        self.str = str
        self.number = number
        print(self.str)
        print(self.number)

    def __add__(self, other):
        print(self.number + ord(self.str[0]))
        return self.number + ord(self.str[0])

    def __sub__(self, other):
        # return self.str[0]
        if self.number > ord(self.str[0]):
            print(self.number - ord(self.str[0]))
            return self.number - ord(self.str[0])

        else:
            print(ord(self.str[0]) - self.number)
            return ord(self.str[0]) - self.number

    def __mul__(self, other):
        print(self.number * ord(self.str[-1]))
        return self.number * ord(self.str[-1])

s1=Myclass('ABC',5)
s2='+'
s4='-'
s6='*'



#Add method
s3=s1+s2
print(s3)


#Subtract method
# s5=s1-s4
# print(s5)

#Multiply method
# s7=s1*s6
# print(s7)


# print(ord('A')+5)
# print(ord('A')-5)
# print(5*ord('C'))
