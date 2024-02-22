"""Create a function called celsius_to_fahrenheit that converts a temperature from Celsius to Fahrenheit using the formula:
fahrenheit = 9/5 * Celsius + 32
The function should take one float input: celsius, and it should return the converted temperature in Fahrenheit as a float. Then call the function at least 3 times, showing the result.
"""

def celsius_to_fahrenheit(celsius):
    # Convert Celsius to Fahrenheit
    fahrenheit = (9/5) * celsius + 32
    return fahrenheit

print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(15))
print(celsius_to_fahrenheit(35))