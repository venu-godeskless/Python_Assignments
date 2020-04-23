"""
Problem 9: Write a regular expression to validate a phone number.
"""
import re
def phone_no(num):
    x12=re.search(re.compile(r'(\+91)?(-)?\s*?(91)?\s*?(\d{3})-?\s*?(\d{3})-?\s*?(\d{4})'), num).group()
    if num ==x12:
        print('Valid Phone Number')
    else:
        print('Not A Valid Phone Number')


phone_no('+919898101353')
phone_no('0359-2595065')
phone_no('0-9778545896')
phone_no('8880344456')
phone_no('08880344456')
phone_no('918880344456')
phone_no('WAQU9876567892')
phone_no('0-9778545896')