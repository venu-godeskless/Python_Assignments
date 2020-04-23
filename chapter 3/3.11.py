"""
Problem 11: Write a python program zip.py to create a zip file.
The program should take name of zip file as first argument and files to add as rest of the arguments.
"""

import os
import zipfile
from zipfile import ZipFile

def Zip(file,add_files):
    zipObj = zipfile.ZipFile(file, 'w')


    for i in add_files:
        zipObj.write(i)
        zipObj.close()

for files in os.listdir():
   print(files)
   Zip('current.zip',files)
