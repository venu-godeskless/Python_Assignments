"""
Problem 14: Create a new virtualenv and install BeautifulSoup. BeautifulSoup is very good library for parsing HTML.
Try using it to extract all HTML links from a webpage.
"""



from bs4 import BeautifulSoup
from urllib.request import urlopen as urls
import html5lib
from html import parser
import requests


url="https://www.flipkart.com/search?q=mobile%20phones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
url_obj=requests.get(url)

soup=BeautifulSoup(url_obj.content,'html5lib')
print(soup.prettify())
r=soup.findAll("div",{"class":"_1DXv5h"})
print(soup.prettify())

print(len(r))     ###----Will show the no. of tags present in that particular class----###
print(r)            ###---will give the tags in list form
print(BeautifulSoup.prettify(r[0]))   ###---will show the tags in that particular class---###
print(r[0])        ###---will give you output in single line----###


new=r[0]

"""---getting one particular tag in that class---"""

name=new.findAll("span",{"class":"_1Dwg_s"})
print(name[0].text)