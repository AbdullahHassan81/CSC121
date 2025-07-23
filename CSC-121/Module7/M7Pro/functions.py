# functions.py
"""
Utility functions for inventory management using product instances.
"""

def category(instances):
    """
    Displays all items in a category.
    
    Parameters:
    instances : list of Product objects
    """
    print(f'\n{"Item":<25}{"Quantity":<15}{"Unit Price"}')
    for instance in instances:
        print(f'{instance.get_name():<25}{instance.get_quantity():<15}${instance.get_unit_price():.2f}')

def get_item(instances, item_name):
    """
    Searches for an item in the list and displays its information.
    
    Parameters:
    instances : list of Product objects
    item_name : str
    """
    for instance in instances:
        if instance.get_name() == item_name:
            print(instance)
            return instance
    print(f'\nThe {item_name} entered was NOT found!')
    return None

def update(instance):
    """
    Updates quantity, unit price, or both for a given Product instance.
    
    Parameters:
    instance : Product object
    """
    if not instance:
        print("No valid item to update.")
        return

    update_choice = int(input("What would you like to update? \n1) Quantity\n2) Price\n3) Both\n"))

    if update_choice == 1:
        qnt = int(input("Enter new Quantity: "))
        instance.set_quantity(qnt)
        print("\nQuantity updated")
    elif update_choice == 2:
        price = float(input("Enter new Price $"))
        instance.set_unit_price(price)
        print("\nUnit Price updated")
    elif update_choice == 3:
        qnt = int(input("Enter new Quantity: "))
        price = float(input("Enter new Price $"))
        instance.set_quantity(qnt)
        instance.set_unit_price(price)
        print("\nQuantity and Unit Price have been updated")
    else:
        print("\nInvalid value entered!!")