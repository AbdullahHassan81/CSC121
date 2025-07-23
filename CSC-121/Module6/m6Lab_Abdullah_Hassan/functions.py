# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 20:16:13 2024

@author: seidih6290
"""


def category(inventory):
    """
    
    Parameters
    ----------
    inventory : nested dictionary for store inventory
    function searches for category entered and displays items under category found

    """
    
    category = input("Enter category(first letter of each word MUST be capitalized): ")

    if category in inventory: # found

        for cat, v in inventory.items():
            if cat == category:
    
                print(f'\n{"Item":<25}{"Quantity":<15}{"Unit Price"}')

                for sub , content in v.items():

                    print(f'{sub:<25}{content["Quantity"]:<15}${content["Unit Price"]}')
    else: 
        # not found
        print(f'\nThe {category} entered was NOT found!')
        
def get_item(inventory):
    
    """
    Parameters
    ----------
    inventory : nested dictionary for store inventory
    function searches for item entered and displays item information

    """
    item = input("Enter Item(first letter MUST be capitalized): ")

    # search in nested dict
    
    item_info = '' # placeholder for cat dictionary

    for cat, v in inventory.items():
        
        if item in v: # get nested dict
            for sub, content in v.items():
        
                if item == sub: 
            
                    item_info = content
            
    if item_info =='': # item not found so no item category dictionary captured
        
        print(f'\nThe {item} entered was NOT found!')
    else:
        
        print(f'\n{"Item":<25}{"Quantity":<15}{"Unit Price"}')

        print(f'{item:<25}{item_info["Quantity"]:<15}${item_info["Unit Price"]}')


            
def update(inventory, item):
    
    """
    Parameters
    ----------
    inventory : nested dictionary for store inventory
    function updates quantity , unit price or both

    """
    for cat, v in inventory.items():

        if item in v: # if found

            #ask what they want to update
            update = int(input("What would you like to update? \n1)Quantity\n2)Price\n3)Both\n"))

            if update == 1: #quantity

                qnt = int(input("Enter new Quantity: "))

                for sub , content in v.items():

                    if sub == item:
                        content["Quantity"]=qnt
                print("\nQuantity updated")
            elif update == 2: # Price

                price = float(input("Enter new Price $"))

                for sub , content in v.items():

                    if sub == item:
                        content["Unit Price"]=price
                print("\nUnit Price updated")
            elif update == 3:

                qnt = int(input("Enter new Quantity: "))
                price = float(input("Enter new Price $"))
                for sub , content in v.items():

                    if sub == item:
                        content["Quantity"]=qnt
                        content["Unit Price"]=price
                                
                print("\nQuantity and Unit Price have been updated")
            else:
                print("\nInvalid value entered!!")
    

          
            
            
    