""" 
A movie theater charges different ticket prices depending on a person's age. If a person is under
the age of 3, the ticket is free; if they are between 3 and 18, the ticket is $10; if they are
between 18 and 65, the ticket is $13; and if they are older than 65, the ticket is $8. Write a 
while loop, where you will ask a user for their age and by using if-elif-else statements, tell the
person what the ticket price will be. After each purchase, ask the user if they want to buy more 
tickets. If they don't, break out of the loop and tell them to have a great time at the movies.
"""

print("Welcome to the Las Vegas Movie Theater. Tonight we are showing the movie Transformers 8: Bumblebee Goes Electric.")
print("The different ticket prices are based on age.")
print("Child under 3: Free")
print("Child between 3 and 18: $10")
print("Adult between 18 and 65: $13")
print("Senior after 65: $8")

flag = True
while flag:
	age = input("\nPlease state your age and I will let you know the price of the ticket: ")
	age = int(age)

	if age <= 3:
		print(f"Since your age is {age}, you will get in for free.")
	elif age <= 18:
		print(f"Since your age is {age}, you will need to pay $10.")
	elif age <= 65:
		print(f"Since your age is {age}, you will need to pay $13.")
	else:
		print(f"Since your age is {age}, you will need to pay $8.")

	answer = input("Would you like to purchase another ticket? Say No if you are done.\nOtherwise just press ENTER. ")
	if answer == "No":
		flag = False

print("Thank you for purchasing your tickets. Have fun with your movie!")

	