import mysql.connector

mydb = mysql.connector.connect(host="localhost",
	                           user='patrik',
	                           passwd='password',
	                           database='tesdb')

mycursor = mydb.cursor()

#Creating a string that can be reused in an execute method
sqlFormula = "INSERT INTO students (name, age) VALUES (%s, %s)"
student1 = ("Rachel", 22)

mycursor.execute(sqlFormula, student1)

mydb.commit()