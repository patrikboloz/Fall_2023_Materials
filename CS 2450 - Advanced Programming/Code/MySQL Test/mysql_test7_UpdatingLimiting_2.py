import mysql.connector

mydb = mysql.connector.connect(host="localhost",
	                           user='patrik',
	                           passwd='password',
	                           database='tesdb')

mycursor = mydb.cursor()

# Selecting just the first 5 values
mycursor.execute("SELECT * FROM students LIMIT 5")

myresults = mycursor.fetchall()
for result in myresults:
	print(result)

print()

# Selecting 5 values, starting from offset 2
mycursor.execute("SELECT * FROM students LIMIT 5 OFFSET 2")

myresults = mycursor.fetchall()
for result in myresults:
	print(result)
