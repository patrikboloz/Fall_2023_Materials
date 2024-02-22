"""Create a function called is_prime that checks if a given positive integer is a prime number. The function should take one integer input: number, and it should return a boolean value (True if the number is prime, False otherwise). Then call the function at least 3 times, showing the result.
"""

def is_prime(number):
    # Check if the number is prime
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

print(is_prime(5))
print(is_prime(6))
print(is_prime(7)) 