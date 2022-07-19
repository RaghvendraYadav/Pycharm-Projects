import mysql.connector as con

mydb=con.connect(host='localhost',user='root',password='0000')
cursor=mydb.cursor()
for i in range(10):
    cursor.execute("insert into FSDS.May2020Batch values('Raghvendra','Paid',24,'1998-02-05');")
mydb.commit()
l=[]
cursor.execute('select * from FSDS.May2020Batch;')
for i in cursor.fetchall():
    l.append(i)

print(l)

