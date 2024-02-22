"""Create a function that calculates the average of numbers. These numbers 
should be given as an arbitrary amount of arguments in the function. Then 
return the average and print out the average."""

def calculate_average(*numbers):
    if not numbers:
        return "No numbers provided."
    total = sum(numbers)
    average = total / len(numbers)
    return average

average1 = calculate_average(10,20,30,40,50)
average2 = calculate_average(10,20)
average3 = calculate_average()

print("Average:", average1)
print("Average:", average2)
print("Average:", average3)

def calculate_average_2(*numbers):
    if  len(numbers) == 0:
        return "No numbers provided."
    total = sum(numbers)
    average = total / len(numbers)
    return average