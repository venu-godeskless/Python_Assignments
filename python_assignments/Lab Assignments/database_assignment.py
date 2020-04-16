"""
Database Assignment
Write a program to display choices to user
1. Insert---- call insertDept function2.
3.
4.
5.
6.
7.
Delete---- call deleteDept – delete a particular record
Update---- call updateDept – update details of particular department
Display All --- call displayAllDept – display only department name
Display ------ call displayDept – display a particular department
Displaydept – will display all the locations which contains or in it
Exit
"""




import mysql.connector
mydb=mysql.connector.connect(
    host = 'localhost',
    user='root',
    password='root',
    database='auth_db',

)
mycursor=mydb.cursor()

"""Creating table --Department--
mycursor.execute("CREATE TABLE department (dept_no INT(10), dept_name VARCHAR(200), dept_location VARCHAR(100))")
"""



"""
Inserted some Data into the table

query="INSERT INTO department (dept_no, dept_name, dept_location) VALUES (%s, %s, %s)"
values=[(1,'sales','mumbai'),
    (2,'development','mumbai'),
    (3,'testing','pune'),
    (4,'management','mumbai'),
    (5,'logistics','delhi'),
    (6,'Hr-Dept','navimumbai'),
    (7,'accounts','bangalore'),
    (8,'research','mumbai')
]

mycursor.executemany(query,values)
# mycursor.execute(query,values)
mydb.commit()
print(mycursor.rowcount,"records inserted")
"""






queries=['1-Insert','2-Delete','3-Update','4-Display All','5-Display','6-DisplayDept']
print('{:>4},{:>4},{:>4},{:>4},{:>4},{:>4}'.format('1-Insert','2-Delete','3-Update','4-Display All','5-Display','6-DisplayDept'))
data_input=int(input("Choose your number betweeen 1 to 6: "))

if data_input==0 or data_input<0 or data_input>6:
    print("Incorrect Number ")

elif data_input == 1:
    dept_no=int(input("enter the dept number: "))
    dept_name=input("enter the department name: ")
    dept_location=input("enter the department location: ")
    query1=("INSERT INTO department (dept_no, dept_name, dept_location) VALUES (%s,%s,%s)")
    values=[dept_no,dept_name,dept_location]
    mycursor.execute(query1,values)
    mydb.commit()
    print("Data entered Successfully")

elif data_input == 2:
    mycursor.execute("SELECT * FROM department")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

    del_id=int(input("delete using id :"))
    query2=("delete from department where dept_no={}".format(del_id))
    mycursor.execute(query2)
    mydb.commit()
    print("Data deleted succesfully")


elif data_input==3:
    mycursor.execute("SELECT * FROM department")
    myresult = mycursor.fetchall()
    x1=[]
    x2=[]
    for x in myresult:
        x1.append(x[1])
        x2.append(x[2])
        print(x)
    update=input("Update details: ")
    dept_no=int(input("Enter the dept_no: "))
    old_detail=input("enter your old entry: ")

    if old_detail in x1:
        mycursor.execute("update department set dept_name=%s where dept_no=%s", (update,dept_no))
        mydb.commit()
        print("record updated succesfully")
    elif old_detail in x2:
        mycursor.execute("update department set dept_location=%s where dept_no=%s",(update,dept_no))
        mydb.commit()
        print("record updated succesfully")


elif data_input==4:
    mycursor.execute("select dept_name from department")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(set(x))


elif data_input==5:
    display_dept=input("enter your name: ")
    mycursor.execute("select * from department where dept_name='{}'".format(display_dept))
    result=mycursor.fetchall()
    for i in result:
        print(i)


elif data_input==6:
    mycursor.execute("select dept_location from department")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(set(x))