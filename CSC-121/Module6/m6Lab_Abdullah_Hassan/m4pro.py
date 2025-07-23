def main():
    inventory = {
        "Desk Supplies": {
            "Pens": {"Quantity": 150, "Unit Price": 3.45},
            "Pencils": {"Quantity": 200, "Unit Price": 1.50},
            "Markers": {"Quantity": 140, "Unit Price": 5.0},
            "Sharpners": {"Quantity": 190, "Unit Price": 1.85}
        },
        "Office Equipment": {
            "Chairs": {"Quantity": 100, "Unit Price": 130},
            "Desks": {"Quantity": 23, "Unit Price": 350.99},
            "Fax machines": {"Quantity": 23, "Unit Price": 400},
            "Calculators": {"Quantity": 15, "Unit Price": 124.89}
        },
        "Computer Accessories": {
            "Flash Drives": {"Quantity": 87, "Unit Price": 54.88},
            "External Hard Drives": {"Quantity": 15, "Unit Price": 174.89},
            "External DVD Drives": {"Quantity": 15, "Unit Price": 84.29}
        }
    }

    choice = 0
    while choice != 5:
        menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            display_inventory(inventory)  # Display inventory and write to CSV
        elif choice == 2:
            category = input("Enter category name (e.g., Desk Supplies): ").title()  # Capitalize input
            category_lookup(inventory, category)
        elif choice == 3:
            item = input("Enter the Item Name (first letter MUST be capitalized): ").title()  # Capitalize input
            item_lookup(inventory, item)
        elif choice == 4:
            item = input("Enter Name of Item you wish to update (first letter MUST be capitalized): ")
            update_inventory(inventory, item)

def display_inventory(inventory):
    print(f'\n{"Category":<30}{"Item":<25}{"Quantity":<15}{"Unit Price":<15}')
    print("-" * 90)
    with open('inventory.csv', 'w') as file:  # Write to CSV file
        file.write("Item name,Quantity,Unit Price,Total\n")  # Header
        for cat, v in inventory.items():
            for sub, content in v.items():
                total_price = content["Quantity"] * content["Unit Price"]
                print(f'{cat:<30}{sub:<25}{content["Quantity"]:<15}${content["Unit Price"]:<15}')
                file.write(f"{sub},{content['Quantity']},{content['Unit Price']},${total_price}\n")  # Write data

def category_lookup(inventory, category):
    if category in inventory:
        print(f'\n{"Item":<25}{"Quantity":<15}{"Unit Price":<15}{"Total":<15}')
        print("-" * 70)
        with open(f"{category}.csv", 'w') as file:
            file.write("Item name,Quantity,Unit Price,Total\n")  # Header
            for sub, content in inventory[category].items():
                total_price = content["Quantity"] * content["Unit Price"]
                print(f'{sub:<25}{content["Quantity"]:<15}${content["Unit Price"]:<15}${total_price:<15}')
                file.write(f"{sub},{content['Quantity']},{content['Unit Price']},${total_price}\n")  # Write data
    else:
        print(f"Category '{category}' not found.")

def item_lookup(inventory, item):
    for category, items in inventory.items():
        if item in items:
            content = items[item]
            total_price = content["Quantity"] * content["Unit Price"]
            print(f'\n{"Item":<25}{"Quantity":<15}{"Unit Price":<15}{"Total":<15}')
            print(f'{item:<25}{content["Quantity"]:<15}${content["Unit Price"]:<15}${total_price:<15}')
            with open(f"{item}.csv", 'w') as file:
                file.write("Item name,Quantity,Unit Price,Total\n")  # Header
                file.write(f"{item},{content['Quantity']},{content['Unit Price']},${total_price}\n")  # Write data
            return
    print(f"Item '{item}' not found.")

def update_inventory(inventory, item):
    # Implementation for updating inventory should be here
    print(f"Update logic for '{item}' should go here.")  # Placeholder; implement as needed

if __name__ == "__main__":
    main()