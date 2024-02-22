#CS 2450 - Advanced Programming
#9/5/2023
#Assignment 2

"""
Your task is to create two dictionaries: Student Registry and Faculty
Registry. Then by creating and using a function, ask the user for a
name and a title, which then will be added to the appropriate dictionary.
This function should print out the name of the current dictionary
and the name/title combo that was added to the dictionary. The 
function should return the dictionary you're working with.
Then by using a for loop, run the function over the student registry
dictionary at least 3 times and over the faculty registry at least 2
times. Then in the end, print out both dictionaries to the terminal.
Also, add a docstring describing what your function is doing. 

Hints:
Create two dictionaries called Student Registry and Faculty Registry.
The first key/value pair will be the key Name_of_dictionary and value
as the actual name of the dictionary.
Create a function that as an argument will have a general dictionary.
Use f-strings which will help with the print statements.
Use the range() function to create a for loop.
Use the standard print function to print out the dictionaries.

"""

student_registry = {"Name_of_dictionary":"Student Registry"}
faculty_registry = {"Name_of_dictionary":"Faculty Registry"}

def add_to_registry(dictionary):
	""" This function takes a dictionary argument and will ask a user
	    to add a person with a title to a dictionary. It will then
	    return the said dictionary.
	"""

	print("You are using a function to add a name/title pair to a dictionary.")
	print(f"The name of the dictionary is: {dictionary['Name_of_dictionary']}")
	person = input("What is the name of this person? ")
	title = input("What is the title of this person? ")
	dictionary[person] = title
	print(f"The person named {person} with the title {title} has been added to the dictionary.\n")
	return dictionary

for i in range(0, 1):
	student_registry = add_to_registry(student_registry)

for i in range(0, 1):
	faculty_registry = add_to_registry(faculty_registry)

print("The updated student registry: ", student_registry)
print("The updated faculty registry: ", faculty_registry)
