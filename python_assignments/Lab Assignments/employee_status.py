"""

Write a program to accept empno,employee name, Salary,Designation
empno:empname:salary:designation
write the details into a file empdata.dat
Write another program to read contents from the file
If designation is
manager then add bonus=2000 in the salary and display on the screen
analyst then add bonus=1500 in the salary
otherwise add bonus=1000 in the salary

"""



import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user='root',
    password='root',
    database='auth_db',

)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM employee_details")
myresult = mycursor.fetchall()
for x in myresult:
        print(x)



"""
#--CREATING A TABLE IN DATABASE
# mycursor.execute("CREATE TABLE employee_details (emp_no INT(20), emp_name VARCHAR(255), salary VARCHAR(255), designation VARCHAR(255))")

"""
#Changed the datatype of emp_no from int to varchar
#alter table auth_db.employee_details modify emp_no varchar(15);
"""

sql = "INSERT INTO employee_details (emp_no, emp_name, salary, designation) VALUES (%s, %s, %s, %s)"
val = [("7219599919" ,"venu", "17000", "developer"),
       ("9527258994","raju","25000","data_fetcher"),
       ("8467394348","rajesh","32810","big_data_er"),
       ("9822690056","prakash","40000","medical_owner"),
       ("8087066607","niels","100000","ml-engineer")]
mycursor.executemany(sql, val) #--inserting multiple record at a time
mycursor.execute(sql,val) #---inserting one record at a time

mydb.commit()

print(mycursor.rowcount,"rows_inserted.")
"""


##--CODE FOR CSV FILE--

import csv
with open("details.csv",'r') as f:
    csv_file=csv.reader(f)
    with open("data.csv","w") as new_file:
        csv_writer=csv.writer(new_file)

        for i in csv_file:
            # print(i)
            eno = i[0]
            varen = i[1]
            varsal = int(i[2])
            vardesig = i[3]
            emp_data=[]

            if vardesig == 'manager':
                emp_data.append(eno)
                emp_data.append(varen)
                emp_data.append(varsal+2000)
                emp_data.append(vardesig)
                csv_writer.writerow(emp_data)


            elif vardesig == 'analyst':
                emp_data.append(eno)
                emp_data.append(varen)
                emp_data.append(varsal + 1500)
                emp_data.append(vardesig)
                csv_writer.writerow(emp_data)


            else:
                emp_data.append(eno)
                emp_data.append(varen)
                emp_data.append(varsal + 1000)
                emp_data.append(vardesig)
                csv_writer.writerow(emp_data)
