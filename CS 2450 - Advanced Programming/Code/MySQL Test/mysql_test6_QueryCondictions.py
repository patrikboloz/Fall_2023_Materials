import mysql.connector

mydb = mysql.connector.connect(host="localhost",
	                           user='patrik',
	                           passwd='password',
	                           database='tesdb')

mycursor = mydb.cursor()

#sql = "SELECT * FROM students WHERE age=25"
sql = "SELECT * FROM students WHERE name='Angel'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for result in myresult:
	print(result)