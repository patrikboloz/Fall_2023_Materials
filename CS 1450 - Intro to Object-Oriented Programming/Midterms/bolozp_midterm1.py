"""A number raised to the third power is called a cube. For example, the cube of 2
   is written as 2**3 in Python. Create a list of numbers (num_list) from 1 to
   10. Then create an empty list called cube_list. By using the for loop, raise 
   every number from the num_list to the third power and save the new numbers in
   the cube_list. In the end, print out both the num_list and cube_list by using
   the print statements. 
"""

num_list = [1,2,3,4,5,6,7,8,9,10]
cube_list = []

for number in num_list:
	cube = number ** 3
	cube_list.append(cube)

print(f"These are the original numbers: {num_list}.")
print(f"These are the cubed numbers: {cube_list}")