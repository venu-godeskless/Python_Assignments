"""
Problem 13: Write a program csv2xls.py that reads a csv file and exports it as Excel file.
The prigram should take two arguments.
The name of the csv file to read as first argument and the name of the Excel file to write as the second argument.
"""


import csv

import xlsxwriter

def read_wrire(csv_file,excel_file):

    with open(csv_file,"r",encoding='latin1') as fp:
        new_csv=csv.reader(fp)
        row=0
        workbook = xlsxwriter.Workbook(excel_file)
        worksheet = workbook.add_worksheet()
        for r,rows in enumerate(new_csv):
            for c,col in enumerate(rows):
                worksheet.write(r,c,col)
            row+=1
        workbook.close()

read_wrire('name.csv','new_sheet.xlsx')