
"""
Problem 8: Write a program links.py that takes URL of a webpage as argument and
prints all the URLs linked from that webpage.
"""


import re
import requests
from urllib.request import urlopen
def link(url):
    res=requests.get(url)
    new_text=res.text
    x = re.findall(r'http://[\w.]+.+"', new_text)
    for i in x:
        print(i[:-1])

link('https://www.google.com/')
