import mysql.connector

mydb = mysql.connector.connect(host="localhost",
	                           user='patrik',
	                           passwd='password',
	                           database='tesdb')

mycursor = mydb.cursor()

#Selecting all the rows in the age column
mycursor.execute("SELECT age FROM students")

myresult = mycursor.fetchall()

for row in myresult:
	print(row)

#Selecting one row in the age column
mycursor.execute("SELECT age FROM students")

myresult2 = mycursor.fetchone()

for row in myresult2:
	print(row)