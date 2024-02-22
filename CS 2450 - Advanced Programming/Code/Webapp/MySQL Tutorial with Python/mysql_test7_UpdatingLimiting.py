import mysql.connector

mydb = mysql.connector.connect(host="localhost",
	                           user='patrik',
	                           passwd='password',
	                           database='tesdb')

mycursor = mydb.cursor()

# Updating age for Angel
sql = "UPDATE students SET age = 13 WHERE name = 'Angel'"

mycursor.execute(sql)

mydb.commit()

