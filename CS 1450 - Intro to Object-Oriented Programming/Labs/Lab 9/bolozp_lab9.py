# Define the base class 'Fruit'
class Fruit:
    def __init__(self, name, color, taste):
        self.name = name
        self.color = color
        self.taste = taste

    def display_info(self):
        print(f"Name: {self.name}, Color: {self.color}, Taste: {self.taste}")

    def is_delicious(self):
        print(f"{self.name} is delicious!")

    def is_ripe(self):
        print(f"{self.name} is ripe!")

# Inherit from the 'Fruit' class to create child classes
class Apple(Fruit):
    def __init__(self, name, color, taste, variety):
        super().__init__(name, color, taste)
        self.variety = variety

    def crunchiness_level(self):
        print(f"{self.name} is known for its crispiness!")

class Banana(Fruit):
    def __init__(self, name, color, taste, length):
        super().__init__(name, color, taste)
        self.length = length

    def peel(self):
        print(f"Peeling a {self.name}.")

class Orange(Fruit):
    def __init__(self, name, color, taste, citrus_type):
        super().__init__(name, color, taste)
        self.citrus_type = citrus_type

    def extract_juice(self):
        print(f"Squeezing an {self.name} to extract juice!")

# Create objects from each child class
apple = Apple("Apple", "Red", "Sweet", "Fuji")
banana = Banana("Banana", "Yellow", "Sweet", "Baby")
orange = Orange("Orange", "Orange", "Citrusy", "Navel")

# Display information and perform unique actions for each object
print("Displaying information about each child class:")
apple.display_info()
apple.crunchiness_level()
print("\n")

banana.display_info()
banana.peel()
print("\n")

orange.display_info()
orange.extract_juice()
