"""
Problem 10: Write a program myip.py to print the external IP address of the machine.
Use the response from http://httpbin.org/get and read the IP address from there.
The program should print only the IP address and nothing else.
"""


import urllib.request

# external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
external_ip = urllib.request.urlopen('http://httpbin.org/get').read().decode('utf8')

print(external_ip)