import mysql.connector

mydb = mysql.connector.connect(host="localhost",
	                           user='patrik',
	                           passwd='password',
	                           database='tesdb')

mycursor = mydb.cursor()

sql = "DELETE FROM students WHERE name = 'Rachel'"
#sql = "DROP TABLE students" #will delete the table
#sql = "DROP TABLE IF EXISTS students" #will delete the table if it exists

mycursor.execute(sql)

#Whenever you update, delete, modify the table, you need to commit the changes.
mydb.commit()