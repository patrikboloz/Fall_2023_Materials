import mysql.connector

# Establish a connection to the MySQL server
connection = mysql.connector.connect(
    host="localhost",
    user="patrik",
    password="password"
)


# Create a cursor to execute SQL commands
cursor = connection.cursor()

# 0. Run to delete the database before using it, if it exists:
cursor.execute("DROP DATABASE assignment2_v2")

# 1. Database Creation
cursor.execute("CREATE DATABASE assignment2_v2")
cursor.execute("USE assignment2_v2")

# 2. Table Creation
cursor.execute("CREATE TABLE Family_Guy (person_id INT PRIMARY KEY, first_name VARCHAR(50), last_name VARCHAR(50), age INT)")

# Print the current table information after creating the table
cursor.execute("DESC Family_Guy")
print("2. Table Creation")
print("Table 'Family_Guy' was created.")
print("Table structure for Family_Guy:")
for column in cursor:
    print(column)
print("=========================\n")

# 3. Data Insertion
insert_query = "INSERT INTO Family_Guy (person_id, first_name, last_name, age) VALUES (%s, %s, %s, %s)"
data = [
    (1, 'Peter', 'Griffin', 45),
    (2, 'Stewie', 'Griffin', 1),
    (3, 'Glenn', 'Quagmire', 54),
    (4, 'Joe', 'Swanson', 42),
    (5, 'Cleveland', 'Brown', 47)
]
cursor.executemany(insert_query, data)
connection.commit()

# Print the current table information after inserting data
cursor.execute("SELECT * FROM Family_Guy")
print("3. Data Insertion")
print("Table data after insertion:")
for row in cursor:
    print(row)
print("=========================\n")

# 4. Data Modification
update_query = "UPDATE Family_Guy SET age = %s WHERE person_id = %s"
cursor.execute(update_query, (50, 1))
connection.commit()

# Print the current table information after modifying data
cursor.execute("SELECT * FROM Family_Guy")
print("4. Data Modification:")
print("Table data after modification:")
for row in cursor:
    print(row)
print("=========================\n")

# 5. Data Deletion
delete_query = "DELETE FROM Family_Guy WHERE person_id = %s"
cursor.execute(delete_query, (2,))
connection.commit()

# Print the current table information after deleting data
cursor.execute("SELECT * FROM Family_Guy")
print("5. Data Deletion:")
print("Table data after deletion:")
for row in cursor:
    print(row)
print("=========================\n")

# 6. Querying the Database
select_query = "SELECT * FROM Family_Guy WHERE age > %s"
cursor.execute(select_query, (50,))
result = cursor.fetchall()

# Print the result of the query
print("6. Data Querying:")
print("Table data after querying:")
for row in result:
    print(row)
print("=========================\n")

# Close the cursor and the connection
cursor.close()
connection.close()


