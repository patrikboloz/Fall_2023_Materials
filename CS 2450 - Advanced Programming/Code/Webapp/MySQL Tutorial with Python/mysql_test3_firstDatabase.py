import mysql.connector

mydb = mysql.connector.connect(host="localhost",
	                           user='patrik',
	                           passwd='password')

#Creating a cursors that communicates with the MySQL
#server
mycursor = mydb.cursor()

#Creating a database called testdb
#Just need to run ONE time.
#mycursor.execute("CREATE DATABASE tesdb")

#Printing out all databases present for patrik
mycursor.execute("SHOW DATABASES")

for db in mycursor:
	print(db)

