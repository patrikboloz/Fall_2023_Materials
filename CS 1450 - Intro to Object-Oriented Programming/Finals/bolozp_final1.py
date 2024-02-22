
grocery_list = []  # Initialize an empty list to store grocery items
add_more_items = True

print("Welcome to the Target!")

while add_more_items:
    item = input("Do you want to add an item to your grocery list? (yes/no): ")

    if item == 'yes':
        grocery_item = input("Enter the item you want to add: ")
        grocery_list.append(grocery_item)
    elif item == 'no':
        add_more_items = False
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

print()
print("\nYour Grocery List:")
for i in grocery_list:
    print(i)