Project Title: Python Restaurant Ordering System
Overview of the Project
The Python Restaurant Ordering System is a command-line interface (CLI) application designed to simulate a simple digital menu and ordering process. It allows customers to view a menu, select multiple items, and automatically calculates the total bill. This project demonstrates fundamental Python concepts including dictionaries, loops, conditional logic, and user input handling.

Features
Interactive Menu Display: Clearly displays available food items and their prices in Rupees (Rs).

Multi-Item Ordering: Utilizes a while loop to allow users to order as many items as they want in a single session without restarting the program.

Input Validation:

Checks if the ordered item exists in the menu.

Handles case sensitivity (e.g., accepts "Pizza", "PIZZA", or "pizza").

Alerts the user if an item is not available.

Dynamic Bill Calculation: Continuously updates the total cost as items are added.

User-Friendly Interface: Includes decorative separators and clear prompts for a better user experience.

Technologies/Tools Used
Programming Language: Python 3.x

Instructions for Testing
To ensure the project works correctly, follow these test cases:

Test Case 1: Ordering a valid item

Run the program.

When prompted, type pizza.

Expected Output: "Your item pizza has been added to your order."

Test Case 2: Handling Case Sensitivity

When asked for an item, type PASTA (in all caps).

Expected Output: The system should recognize "pasta" and add Rs50 to the total.

Test Case 3: Ordering an invalid item

When asked for an item, type sandwich.

Expected Output: "Ordered item sandwich is not available yet!"

Test Case 4: Finishing the Order

After adding items, when asked "Do you want to add another item?", type no.

Expected Output: The loop terminates, and the final total (e.g., "The total amount of items to pay is Rs90") is displayed.

