"""
Problem 2.18: Write a program to print each line of a file in reverse order.
"""


with open("she.txt","r") as f:
    x5=open("new_text.txt","w")

    y5=f.readlines()
    for line in y5:
        x5.writelines(reversed(line))
