import mysql.connector

mydb = mysql.connector.connect(host="localhost",
	                           user='patrik',
	                           passwd='password',
	                           database='tesdb')

mycursor = mydb.cursor()

#Creating a string that can be reused in an execute method
sqlFormula = "INSERT INTO students (name, age) VALUES (%s, %s)"
students = [("Bob", 25),
            ("Angel", 42),
            ("Jacob", 92),
            ("Richard", 27),
            ("Jaime", 20)]

mycursor.executemany(sqlFormula, students)

mydb.commit()