"""A pangram is a sentence that contains all the letters of the English alphabet at least
once, for
example: The quick brown fox jumps over the lazy dog.
Your task here is to write a function to check asentence to see if it is a pangram or not."""

# ANS--
n=input("enter your string here: ")
n1=n.lower()
# print(n1)--all lower cases
n1=set(n1)
# print(n1)--prints all unique values
x=''
# print(x)-- printing x

spaces=["'"," ",",","'",".",":",";"]
for i in n1:
    if i in spaces:
        pass
    else:
        x+=i
# x=''.join(pass if i in spaces else x+=i for i in n1 )


# if len(x)!=26:
#     print('string is not pangram')
# else:
#     print('given string is pangram')


print('string is not pangram') if len(x)!=26 else print("string is pangram")