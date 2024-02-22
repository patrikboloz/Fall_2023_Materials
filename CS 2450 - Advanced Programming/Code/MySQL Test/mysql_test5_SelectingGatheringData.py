import mysql.connector

mydb = mysql.connector.connect(host="localhost",
	                           user='patrik',
	                           passwd='password',
	                           database='tesdb')

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM students")

myresult = mycursor.fetchall()

for row in myresult:
	print(row)