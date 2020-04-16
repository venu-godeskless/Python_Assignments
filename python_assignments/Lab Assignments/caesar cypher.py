"""
In cryptography, a Caesar cipher is a very simple encryption techniques in which
each letter in the
plain text is replaced by a letter some fixed number of positions down the alphabet.
For example, with a
shift of 3, A would be replaced by D, B would become E, and so on. The method is
named after Julius
Caesar, who used it to communicate with his generals. ROT-13 ("rotate by 13
places") is a widely used
example of a Caesar cipher where the shift is 13. In Python, the key for ROT-13 may
be represented by
means of the following dictionary:key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t',
'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c',
'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q',
'E':'R', 'F':'S', 'G':'T',
'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F',
'T':'G', 'U':'H', 'V':'I',
'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}
Your task in this exercise is to implement an encoder/decoder of ROT-13. Once
you're done, you will be
able to read the following secret message:
Pnrfnepvcure? V zhpucersrePnrfnefnynq!
Note that since English has 26 characters, your ROT-13 program will be able to both
encode and decode
texts written in English.
"""

n= input("enter the string: ")
steps=int(input("enter the shifts"))

x=[]
y=[]

upper=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']

lower=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']

for i in n:
    if i in upper:
        index1=upper.index(i)
        # print(index1)
        num1=(index1+steps)%26
        # print(num1)
        new=upper[num1]
        # print(new)
        x.append(new)


    elif i in lower:
        index2=lower.index(i)
        # print(index2)
        num2=(index2+steps)%26
        # print(num2)
        new=lower[num2]
        # print(new)
        x.append(new)



x=''.join(x)
print(x)