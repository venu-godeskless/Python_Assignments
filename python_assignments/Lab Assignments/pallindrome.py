"""
Write a version of a palindrome recognizer that also accepts phrase palindromes such
as "Go hanga salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a
potato pan, Otis", "Lisa
Bonet ate no basil", "Satan, oscillate my metallic sonatas", "I roamed under it as a tired
nude Maori",
"Rise to vote sir", or the exclamation "Dammit, I'm mad!". Note that punctuation,
capitalization, and
spacing are usually ignored.
"""

# ANS--
n = input("enter your string here:")
n=n.casefold()
# n=n.lower()
# print(n)--prints converted string
x=''

c=[".",",","'","''"," ","?","  "]
for i in n:
    if i in c:
        pass
    else:
        x+=i
# print(x)--printing x after removing punctuations
v=x[::-1]
# print(v)-- reverse of x


# if x==v:
#     print("string is pallindrome")
# else:
#     print("not a pallindrome")

print("string is pallindrome") if x==v else print("string is not pallindrome")
