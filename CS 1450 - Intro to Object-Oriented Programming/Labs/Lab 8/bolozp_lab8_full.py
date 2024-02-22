class House:
    def __init__(self, num_bathrooms, price, location, status="Not Sold"):
        self.num_bathrooms = num_bathrooms
        self.price = price
        self.location = location
        self.status = status

    def print_num_bathrooms(self):
        print(f"Number of bathrooms: {self.num_bathrooms}")

    def print_price(self):
        print(f"Price: ${self.price}")

    def print_location(self):
        print(f"Location: {self.location}")

    def update_price(self, new_price):
        self.price = new_price
        print("Price updated successfully!")

    def update_status(self, new_status):
        self.status = new_status
        print("Status updated successfully!")

# Create an instance of the House class with initial values
house = House(5, 1000000, "445 Long Road, Las Vegas, NV")

# Display initial information about the house
print("Displaying initial information about the house.")
house.print_num_bathrooms()
house.print_price()
house.print_location()
print(f"Status: {house.status}")
print("==========================\n")

# Update the price and status
print("Updating the price and status")
house.update_price(750000)
house.update_status("Sold")
print("==========================\n")

# Display updated information about the house
print("Displaying information about the house:")
house.print_num_bathrooms()
house.print_price()
house.print_location()
print(f"Status: {house.status}")
print("==========================\n")