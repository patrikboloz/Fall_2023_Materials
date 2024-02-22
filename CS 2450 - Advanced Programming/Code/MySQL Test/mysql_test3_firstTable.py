import mysql.connector

mydb = mysql.connector.connect(host="localhost",
	                           user='patrik',
	                           passwd='password',
	                           database="tesdb")

#Creating a cursors that communicates with the MySQL
#server
mycursor = mydb.cursor()

#Creating a new table in the testdb database
mycursor.execute("CREATE TABLE students (name VARCHAR(255), age INTEGER(10))")

#Show the tables that exist in the database
mycursor.execute("SHOW TABLES")

for tb in mycursor:
	print(tb)
