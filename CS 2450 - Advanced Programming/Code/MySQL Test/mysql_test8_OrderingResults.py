import mysql.connector

mydb = mysql.connector.connect(host="localhost",
	                           user='patrik',
	                           passwd='password',
	                           database='tesdb')

mycursor = mydb.cursor()

#sql = "SELECT * FROM students ORDER BY name"
#sql = "SELECT * FROM students ORDER BY age"
#sql = "SELECT * FROM students ORDER BY age DESC"
sql = "SELECT * FROM students ORDER BY name DESC"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for r in myresult:
	print(r)