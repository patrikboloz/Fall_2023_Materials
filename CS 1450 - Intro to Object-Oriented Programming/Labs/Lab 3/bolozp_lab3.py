#CS 1450
#Patrik Boloz
#9-12-2023

"""
1) Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which 
they live. You should have keys such as first_name, last_name, 
age, and city. Print each piece of information stored in your 
dictionary.

2) Make a dictionary containing three major rivers and the country 
each river runs through. One key-value pair might be 'nile': 'egypt'.
- Use a loop to print a sentence about each river, such as The Nile 
runs through Egypt.
- Use a loop to print the name of each river included in the dictionary.
- Use a loop to print the name of each country included in the dictionary.

3) Create a list of New Mexico/random cities. Then by using another 
variable called city and looping through the list by using a for loop, 
print out a message if the city exists in the list or not (use if/else).
"""

#1
print("========================")
print("Exercise 1:\n")

person_dictionary = {'first_name':'Patrik',
					 'last_name':'Boloz',
					 'age':27,
					 'city':'Poprad'}

"""					 
print(f"The person_dictionary was created and this is how it looks like:")
print(person_dictionary)
"""

print(f"The first name of my person is: {person_dictionary['first_name']}.")
print(f"The last name of my person is: {person_dictionary['last_name']}.")
print(f"The age of my person is: {person_dictionary['age']}.")
print(f"The city of my person is: {person_dictionary['city']}.")

#2
print("========================")
print("Exercise 2:\n")

river_dictionary = {'nile':'egypt',
                    'danube':'slovakia',
                    'mississippi':'usa'}

for river, country in river_dictionary.items():
	print(f"The river {river.title()} runs through {country.title()}.")

print("The rivers in the dictionary are:")
for river in river_dictionary.values():
	print(river.title())

print("The countries in the dictionary are:")
for country in river_dictionary.keys():
	print(country.title())

#3 
print("========================")
print("Exercise 3:\n")

city_list = ["Las Vegas", "Santa Fe", "Albuquerque", "Pecos"]
lookup_city = "Santae"

print(f"The city list is: {city_list}")
flag = False
for city in city_list:	
	if lookup_city == city:
		print(f"The city {lookup_city} was found in the city list!")
		flag = True

if flag == False:
	print(f"The city {lookup_city} was NOT found in the city list!")