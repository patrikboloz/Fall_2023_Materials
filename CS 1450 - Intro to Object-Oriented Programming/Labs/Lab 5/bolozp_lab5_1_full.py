""" Create a function called calculate_triangle_area that calculates the area of a triangle using the formula:
area = 1/2 * base * height
The function should take two float inputs: base and height, and it should return the calculated area as a float. Then call the function at least 3 times, printing out the result. 
""" 

def calculate_triangle_area(base, height):
    # Calculate the area of the triangle
    print(f"The base is {base} and the height is {height}")
    area = 0.5 * base * height
    return area

print(f"The area of the triangle is: {calculate_triangle_area(10, 20)}.\n")
print(f"The area of the triangle is: {calculate_triangle_area(5, 20)}.\n")
print(f"The area of the triangle is: {calculate_triangle_area(2, 20)}.\n")
