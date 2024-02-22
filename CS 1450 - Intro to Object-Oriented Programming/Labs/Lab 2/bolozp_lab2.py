# CS 1450
# Patrik Boloz
# Lab 2

""" 
Exercise 1:
Create a list of 10 random names called names_list. Then by using a 
for loop, that loops through each name, print out each name with a 
message telling them that they should have a good semester.

Exercise 2:
Create a list of numbers from 0 until 150, where the step value will be 5.
Then by using a for loop, multiply the current number by 3 and add that 
number into another newly created list called triple. After the loop ends, 
print out the max, min, and sum values of the triple list.

Exercise 3:
Remove the last item in the names_list and triple. Then show them in the
terminal each with a custom message. 
"""


#Exercise 1

print("Exercise 1")
print("================================")
name_list = ["Patrik", "Jonas", "John", "Richard", "Alex", "Robert", "Aria", "Sansa", "Rupert", "George"]
for name in name_list:
	print(f"I hope you have a great semester, {name}!")

print("================================")

#Exercise 2
print("\nExercise 2")
print("================================")
numbers = list(range(0,150,5))
triple = []

for number in numbers:
	curr_number = number * 3
	triple.append(curr_number)

print("This is the numbers list:", numbers)
print("This is the triple list:", triple, "\n")
print("The max value from the triple list is:", max(triple))
print("The min value from the triple list is:", min(triple))
print("The sum of all values in the triple list is:", sum(triple))
print("================================")

#Exercise 3
print("\nExercise 3")
print("================================")

last_item_numbers = numbers.pop()
last_item_triple = triple.pop()
print(f"The last item in the numbers list is {last_item_numbers}")
print(f"The last item in the triple list is {last_item_triple}")
print("================================")
