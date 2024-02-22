# CS 1450
# Patrik Boloz
# Lab 4

""" For this lab, you will need to finish these two exercises:
1) Imagine you run a dealership and a customer asks you for a car. You need to
   check your invetory and depending on the availability respond if you have/not
   have the car in stock.
   Hints: Create a list of cars. Create a variable called car and use the input()
   function to ask the user for the car. Then by using if/else statemtents, check
   for the membership by using the in operator. Finally print out a message 
   depending if the car was found/not found.

2) Imagine you run a restaurant and you have a group of customers trying to find
   an empty table. Ask the customers how many people are in their group and if
   there are more than 8 people, turn them away.
   Hints: Create a variable that will ask the user how many customers there will
   be. Then by using if-else statements print out a message allowing them into/
   turning them down from the restaurant. Don't forget that any input will be a 
   string and you'll need to convert the string into an integer!
"""

#Exercise 1
print("Exercise 1")
carlist = ["Subaru", "Skoda", "Porsche", "Dodge"]
car = input("What is your car name? ")

if car in carlist:
	print(f"We have the car {car} in stock.")
else:
	print(f"We don't have this vehicle in stock.")


#Exercise 2
print("\n===============================")
print("Exercise 2")
number_of_guests = int(input("Welcome to Thanos' Restaurant, how many people do you have in a group? "))

if number_of_guests <= 8:
	print(f"Please follow me. I'll get you a table for {number_of_guests}.")
else:
	print(f"I apologize for the inconvenience, but you need to set a reservation for groups bigger than 8.")

