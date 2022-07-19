import mysql.connector as con

mydb=con.connect(host='localhost',user='root',password='0000')
cursor=mydb.cursor()
#query="create table FSDS.May2020Batch(name varchar(20),fee_status varchar(20),age int,DOB date);"
query="insert into FSDS.May2020Batch values('Raghvendra','Paid',24,'1998-02-05');"
cursor.execute(query)
cursor.execute('select * from FSDS.May2020Batch;')
for i in cursor.fetchall():
    print(i)
mydb.close()