"""Given a dictionary of students and their favourite colours:
people={'Arham':'Blue','Lisa':'Yellow',''Vinod:'Purple','Jenny':'Pink'}
1. Find out how many students are in the list
2. Change Lisa’s favourite colour
3. Remove 'Jenny' and her favourite colour
4. Sort and print students and their favourite colours alphabetically by name
Write a function translate() that will translate a text into "rövarspråket" (Swedish for
"robber's language").
That is, double every consonant and place an occurrence of "o" in between. For
example, translate("this
is fun") should return the string "tothohisosisosfofunon".
"""

people={'Arham':'Blue','Lisa':'Yellow','Vinod':'Purple','Jenny':'Pink'}

##1--
print("there are {} students in the list".format(len(people)))

## 2--

# x=people['Lisa']='blue'
# print(x)

people['Lisa']='violet'
print(people['Lisa'])

##3--

del people['Jenny']
print(people)

## 4--
# print(sorted(people))
# print(people.keys())
print(sorted(people.items()))

##5--
n=input("enter the string :")

n=n.lower()
consonats='bcdfghjklmnpqrstvwxyz'

x=''
for char in n:
    if char in consonats:
        x+=''.join(char+'o'+char)
    else:
        x+=''.join(char)

    # x += ''.join(char + 'o' + char) if char in consonats else x+= ''.join(char)
print(x)