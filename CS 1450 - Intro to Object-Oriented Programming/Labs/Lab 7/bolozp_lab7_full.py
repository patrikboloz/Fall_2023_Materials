""" Create a Lizard class that will have these initial
parameters: name, age, color. The lizard should be able
to go to sleep, run, and change color. Also include a 
method that will print out its current name, age, and
color. Then create at least 3 lizards and use each method 
at least once. 
"""

class Lizard:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def sleep(self):
        print(f"{self.name} the lizard is going to sleep.")

    def run(self):
        print(f"{self.name} the lizard is running.")

    def change_color(self, new_color):
        self.color = new_color
        print(f"{self.name} the lizard has changed color to {self.color}.")

    def get_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Color: {self.color}")

# Create at least three instances of the Lizard class
lizard1 = Lizard("Cilly", 3, "Yellow")
lizard2 = Lizard("Spooky", 1, "White")
lizard3 = Lizard("Fuego", 5, "Red")

# Demonstrate the behavior of the lizards
lizard1.sleep()
lizard1.run()
lizard1.change_color("Orange")
lizard1.get_info()
print()

lizard2.run()
lizard2.change_color("Green")
lizard2.get_info()
print()

lizard3.sleep()
lizard3.get_info()
