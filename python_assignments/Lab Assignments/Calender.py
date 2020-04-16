"""Write a program that asks the user how many days are in a particular month, and what
day of the
week the month begins on (0 for Monday, 1 for Tuesday, etc), and then prints a calendar for
that month.
For example, here is the output for a 30-day month that begins on day 4 (Thursday):
S M T W T F S
1 2 3
4 5 6 7 8 9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30"""


no_of_days = int(input("enter the number of days in the month: "))
start_Date = input("enter the the day to start month:")
start_Date=start_Date.capitalize()

days=['Su','M','T','W','Th','F','S']

# --Printing days with the help of string formating
print('{:>3}{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}'.format('Su','M','T','W','Th','F','S'))


# for i in range(1,no_of_days+1):
#     if i==1 and start_Date==days[0]:
#         print('{:>3}'.format(i),end='')
#     elif i==1 and start_Date==days[1]:
#         print(''*4+'{:>3}'.format(i),end='')
#     elif i==1 and start_Date==days[2]:
#         print(''*8+'{:>3}'.format(i),end='')
#     elif i==1 and start_Date==days[3]:
#         print(''*12+'{:>3}'.format(i),end='')
#     elif i==1 and start_Date==days[4]:
#         print(''*16+'{:>3}'.format(i),end='')
#     elif i==1 and start_Date==days[5]:
#         print(''*20+'{:>3}'.format(i),end='')
#     elif i==1 and start_Date==days[6]:
#         print(''*24+'{:>3}'.format(i),end='')
#     else:
#         print('{:>3}'.format(i),end='')

for i in range(1,no_of_days+1):
  if start_Date==days[0] and i ==1:
    print('{:>3}'.format(i),end =' ')
  elif start_Date==days[1] and i ==1:
    print(' '*4+'{:>3}'.format(i),end =' ')
  elif start_Date==days[2] and i ==1:
    print(' '*8+'{:>3}'.format(i),end =' ')
  elif start_Date==days[3] and i ==1:
    print(' '*12+'{:>3}'.format(i),end =' ')
  elif start_Date==days[4] and i ==1:
    print(' '*16+'{:>3}'.format(i),end =' ')
  elif start_Date==days[5] and i ==1:
    print(' '*20+'{:>3}'.format(i),end =' ')
  elif start_Date==days[6] and i ==1:
    print(' '*24+'{:>3}'.format(i),end =' ')
  else:
    print('{:>3}'.format(i),end =' ')

    if i%7==0 and start_Date==days[0]:
        print()
    elif i%7==6 and start_Date==days[1]:
        print()
    elif i%7==5 and start_Date==days[2]:
        print()
    elif i%7 == 4 and start_Date==days[3]:
        print()
    elif i%7==3 and start_Date==days[4]:
        print()
    elif i%7 == 2 and start_Date==days[5]:
        print()
    elif i%7 ==1 and start_Date==days[6]:
        print()


