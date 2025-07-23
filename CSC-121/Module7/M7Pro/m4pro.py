import functions as fn
import csv
from functions import category, get_item, update

class Product:
    def __init__(self, name, quantity, unit_price):
        self._name = name
        self._quantity = quantity
        self._unit_price = unit_price

    def set_quantity(self, quantity):
        self._quantity = quantity

    def set_unit_price(self, price):
        self._unit_price = price

    def get_name(self):
        return self._name

    def get_quantity(self):
        return self._quantity

    def get_unit_price(self):
        return self._unit_price

    def get_total(self):
        return self._quantity * self._unit_price

    def __repr__(self):
        return (f"{self.__class__.__name__}(Name: {self._name}, "
                f"Quantity: {self._quantity}, Unit Price: {self._unit_price}, "
                f"Total: {self.get_total()})")


def create_instance(category, items):
    """
    Create Product instances from dictionary data.
    """
    return [Product(item, details["Quantity"], details["Unit Price"])
            for item, details in items.items()]


def write_instance(category, instances):
    """
    Write product data to CSV file.
    """
    filename = f"{category}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Item", "Quantity", "Unit Price", "Total"])
        for instance in instances:
            writer.writerow([instance.get_name(), instance.get_quantity(),
                             f"${instance.get_unit_price():.2f}", f"${instance.get_total():.2f}"])


def main():
    """
    Main program loop to handle inventory management.
    """
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

    category_instances = {cat: create_instance(cat, items) for cat, items in inventory.items()}

    choice = 0
    while choice != 5:
        print("\n---------Menu---------")
        print("1) Display Inventory Content")
        print("2) Category Lookup")
        print("3) Item Lookup")
        print("4) Update Item Info")
        print("5) Exit")
        print("----------------------\n")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            for cat, instances in category_instances.items():
                print(f"\nCategory: {cat}")
                category(instances)
                write_instance(cat, instances)

        elif choice == 2:
            cat_name = input("Enter category (Desk Supplies, Office Equipment, Computer Accessories): ")
            if cat_name in category_instances:
                category(category_instances[cat_name])
            else:
                print("Category not found.")

        elif choice == 3:
            cat_name = input("Enter category name: ")
            if cat_name in category_instances:
                item_name = input("Enter item name: ")
                get_item(category_instances[cat_name], item_name)
            else:
                print("Category not found.")

        elif choice == 4:
            cat_name = input("Enter category name: ")
            if cat_name in category_instances:
                item_name = input("Enter item name: ")
                instance = get_item(category_instances[cat_name], item_name)
                update(instance)
                write_instance(cat_name, category_instances[cat_name])
            else:
                print("Category not found.")

        elif choice == 5:
            print("Program terminating....")
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()