import mysql.connector

mydb = mysql.connector.connect(host="localhost",
	                           user='patrik',
	                           passwd='password',
	                           database='tesdb')

mycursor = mydb.cursor()

# Query using wildcards, % - wildcard
sql = "SELECT * FROM students WHERE name LIKE 'R%'"
#sql = "SELECT * FROM students WHERE name LIKE '%i%'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for result in myresult:
	print(result)

#SQL Injection
sql = "SELECT * FROM students WHERE name = %s"
mycursor.execute(sql, ('Angel', )) #needs to be a tuple
myresult = mycursor.fetchall()

for result in myresult:
	print(result)