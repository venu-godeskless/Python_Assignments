"""
Problem 2.17: Write a program reverse.py to print lines of a file in reverse order.
"""


file=open("she.txt","w")
l=["She sells seashells on the seashore;\n"
"The shells that she sells are seashells I'm sure.\n"
"So if she sells seashells on the seashore,\n"
"I'm sure that the shells are seashore shells.\n"]
file.writelines(l)
file.close()


##-----1st method---###
file1=open("she.txt","r")
line=file1.readlines()
for i in reversed(line):
    print(i)

###---2nd method---###
file1=open("she.txt","r")
line=reversed(file1.readlines())
for i in line:
    print(i)


###---3rd method---###
filename=input("Enter file name: ")
for line in reversed(list(open(filename))):
    print(line.rstrip())
