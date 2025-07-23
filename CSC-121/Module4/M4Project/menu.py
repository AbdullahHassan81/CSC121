import mainInventory as mi
#somewhat incomplete 
#have to display office supplies and computer accessories 


def menu():
    print("---------------Menu---------------")
    print("1) Display Inventory")
    print("2) Category Lookup")
    print("3) Item Lookup")
    print("4) Update Item Info")
    print("5) Exit")
    print("----------------------------------")

def category_lookup(inventory):
    """Lookup items by category."""
    print("Existing categories:", ', '.join(inventory.keys()))  # Display existing categories
    category_name = input("Enter the category name: ")

    if category_name in inventory:
        print(f'{"Item":<20}{"Quantity":<10}{"Unit Price":<10}')
        # Loop through each item in the specified category
        for item, details in inventory[category_name].items():
            print(f'{item:<20}{details["Quantity"]:<10}{details["Unit Price"]:<10}')
    else:
        print("Category not found. Please try again.")

def item_lookup(inventory):
    """Lookup item by name."""
    item_name = input("Enter the item name: ")  # Ask user to enter item name
    item_found = False  # Flag to check if item is found

    print(f'{"Item":<20}{"Quantity":<10}{"Unit Price":<10}')  # Table header
    for categories in inventory.values():
        if item_name in categories:
            details = categories[item_name]
            print(f'{item_name:<20}{details["Quantity"]:<10}{details["Unit Price"]:<10}')  # Display item info
            item_found = True

    if not item_found:
        print("Item not found. Please try again.")  # Notify user if item not found

def update_item_info(inventory):
    item_name = input("Enter the item name to update: ")
    item_found = False

    # Check if the item exists in the inventory
    for categories in inventory.values():
        if item_name in categories:
            item_found = True
            choice = input("What do you want to update? (Quantity/Unit Price): ").strip().lower()

            if choice == "quantity" or choice == "unit price":
                new_value = input(f"Enter new value for {choice}: ")
                if choice == "quantity":
                    categories[item_name]["Quantity"] = int(new_value)  # Update Quantity
                else:
                    categories[item_name]["Unit Price"] = float(new_value)  # Update Unit Price
                print(f'{item_name} updated successfully.')
            else:
                print("Invalid option. Please choose either 'Quantity' or 'Unit Price'.")
            break  # Exit the loop after processing the update

    if not item_found:
        print("Item not found. Please try again.")

#Main Loop
choice = 0
while choice !=5:
    menu()

    choice = int(input("Enter choice: "))

    if choice == 1:
        print(f'{"Category":<20}{"Item":<20}{"Quantity":<10}{"Unit Price":<10}')
        inventory = mi.main()  # Get the inventory from mainInventory

        # Loop through each category and each item in the category
        for category, items in inventory.items():
            for item, details in items.items():
                print(f'{category:<20}{item:<20}{details["Quantity"]:<10}{details["Unit Price"]:<10}')
            print()  # Print a newline for better readability

    elif choice ==2: 
        inventory = mi.main()  # Get the inventory from mainInventory
        category_lookup(inventory)  # Call the category lookup function

    elif choice ==3: 
        inventory = mi.main()  # Get the inventory from mainInventory
        item_lookup(inventory)  # Call the item lookup function
    elif choice == 4:  # Call the new function when user selects option 4
        inventory = mi.main() 
        update_item_info(inventory)
    elif choice ==5:
        print("Program Exiting")