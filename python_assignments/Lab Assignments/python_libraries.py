"""

(numpy,pandas,matplotlib,scipy)

1. Complete following program
import pandas as pd
mymoviedata=pd.read_table("http://bit.ly/movieusers",sep="|",header=None)
print(mymoviedata.head())
# add headings to the column- col1,col2,col3,col4,col5
#display only column col3
#add col6 concatenate values of col2 and col3 and seperate them by :
# retrieve values of col1 and col4 display bar graph
# display names of all the columns.


2.
#create a list for storing year 2010 to 2014
#create a list for each year for storing sales amout for of 5 products in each years
#draw pie chart and stack graph to compare sales

"""






from matplotlib import pyplot as plt
import pandas as pd



## 1---

# mymoviedata=pd.read_csv("http://bit.ly/movieusers",sep="|")
# mymoviedata=pd.read_csv("http://bit.ly/movieusers",sep="|",header=None)
# print(mymoviedata.head())


##----add headings to the column- col1,col2,col3,col4,col5-----
mymoviedata=pd.read_csv("http://bit.ly/movieusers",sep="|",names=["No.","Age","Sex","Profile","Salary"])
# print(mymoviedata.head())



# mymoviedata.columns=["No.","Age","Sex","Profile","Salary"]##--It will consider the first row as header before naming columns
# print(mymoviedata.head())



##----display only column col3----
# print(mymoviedata.head()['Sex'])





##-----add col6 concatenate values of col2 and col3 and seperate them by :----
# 1--method -1
mymoviedata['new_column']=mymoviedata['Age'].astype(str) +' : ' + ['Sex']
# print(mymoviedata.head()['new_column'])

#method-2
mymoviedata['combined']=mymoviedata.apply(lambda x:'%s : %s' % (x['Age'],x['Sex']),axis=1)
# print(mymoviedata.head()['combined'])



###-----retrieve values of col1 and col4 display bar graph------

# x=mymoviedata.head()['No.']
# y=mymoviedata.head()['Salary']

# plt.bar(x,y,width=0.5,color='blue')
# plt.xlabel('x-label')
# plt.ylabel('y-label')
# plt.title('BAR-GRAPH')
# plt.show()



###------ display names of all the columns.--------
# print(mymoviedata.columns.values)



# 2----

# years=['2010','2011','2012','2013','2014','2015']
# sales=[10, 130, 245, 210,100,20]

# explode=(0.1, 0, 0, 0,0,0)
# colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','red']
# plt.pie(sales, explode=explode, labels=years, colors=colors,autopct='%1.1f%%', shadow=True, startangle=180)
# plt.show()
team=['Backend','IoS','Android','Angular','QA']
peoples=['13','2','2','3','3']
backend=['Mayuri','Sharayu','Vijay','Ketan','Dhananjay','Nilesh.K','Nikhil',
         'Akshay','Dhanashree','Pratiksha','Paurnima','Shivani','Venu']
ios=['Nilesh.P','Ganesh']
angular=['Ketan','Shivani','Dhananjay']
android=['Sreekant','Prashant']
Qa=['Himabindu','Pranith','Shraddha']


explode=(0.1,0,0,0,0)
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','red']
plt.pie(peoples, explode=explode,labels=team, colors=colors,autopct='%1.1f%%', shadow=True, startangle=180)
# plt.legend(backend,ios)
# plt.axis("off")
plt.legend([backend,ios,android,angular,Qa],loc="lower center")
plt.show()
