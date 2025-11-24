# Define the menu of restaurant
menu = {'pizza': 40, 'pasta': 50, 'burger': 60, 'salad': 70, 'hot coffee': 40, 'cold coffee': 80}
# Greet
print("Welcome to Python Restaurant")
print("pizza: Rs40\npasta: Rs50\nburger: Rs60\nsalad: Rs70\nhot coffee: Rs40\ncolf coffee: Rs80")

order_total = 0

# Ask for the first item
item_1 = input("Enter the name of item you want to order = ")

# Check if item exists in menu
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not available yet!")

# Ask if the user wants to add another item
another_order = input("Do you want to add another item? (yes/no) ")

if another_order == "yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]+menu[item_1]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Ordered item {item_2} is not available!")

# Display total amount

print(f"The total amount of items to pay is {order_total}")
