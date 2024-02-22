"""Write a function that accepts a list/tuple of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the sand-
wich that’s being ordered. Call the function three times, using a different num-
ber of arguments each time"""

def make_sandwich(*items):
    print("Sandwich order summary:")
    if items:
        print("You've ordered a sandwich with the following items:")
        for item in items:
            print(item)
    else:
        print("You haven't ordered any items for your sandwich.")
    print()

make_sandwich("Tuna Salad")
make_sandwich("Pepperoni", "Ham", "Lettuce")
make_sandwich("Turkey", "Bacon", "Salami", "Tomato")
make_sandwich()

