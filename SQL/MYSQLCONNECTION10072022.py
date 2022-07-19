import mysql.connector as con

mydb=con.connect(host='localhost',user='root',password='0000')
print(mydb)
cursor=mydb.cursor()
cursor.execute('show databases')
print(cursor.fetchall())
mydb.close()
