# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 09:51:52 2024

@author: seidih6290
"""

import functions as fn
def main():

    # inventory defined below

    inventory = {"Desk Supplies":{"Pens":{"Quantity":150,"Unit Price":3.45},"Pencils":{"Quantity":200,"Unit Price":1.50},
    "Markers":{"Quantity":140,"Unit Price":5.0} ,"Sharpners":{"Quantity":190,"Unit Price":1.85} },"Office Equipment":{"Chairs":{"Quantity":100,"Unit Price":130},
       "Desks":{"Quantity":23,"Unit Price":350.99},"Fax machines":{"Quantity":23,"Unit Price":400},
       "Calculators":{"Quantity":15,"Unit Price":124.89}},"Computer Accessories":{"Flash Drives":{"Quantity":87,"Unit Price":54.88},
       "External Hard Drives":{"Quantity":15,"Unit Price":174.89},"External DVD Drives":{"Quantity":15,"Unit Price":84.29} }}
 
    choice = 0 # initial value of 0 assigned to choice so that the menu is displayed the first time the program is executed

    while choice != 5: # option 5 means the user wants to terminate

        menu()
        choice = int(input("Enter your choice: "))     
        if choice == 1:# display content
            
            
            print(f'\n{"Category":<30}{"Item":<25}{"Quantity":<15}{"Unit Price"}')
            print("-"*70)
            
            for cat, v in inventory.items():
                
                
                for sub , content in v.items():
                    
                   print(f'{cat:<30}{sub:<25}{content["Quantity"]:<15}${content["Unit Price"]}')
        elif choice ==2: # # category lookup
            
            fn.category(inventory) # calls the function that performs the search


        elif choice ==3:  # items search
            
            fn.get_item(inventory)

        elif choice == 4: #update

            item = input("Enter Name of Item you wish to update(first letter MUST be capitalized): ")

            # search in nested dict

            fn.update(inventory, item)
        elif choice == 5:

            print("Program terminating....")
        else:

            print("\nInvalid Entry!!")

                                                                                  
def menu():
    """
    function display menu options, doesn't retrun a value
    """
    # print statements below display menu
    
    print("\n---------Menu---------")
    print("1) Display Inventory Content")
    
    print("2) Category Lookup")
    
    print("3) Item Lookup")
    print("4) Update Item Info")
    print("5) Exit")
    
    print("----------------------\n")
                                                                               
                                                                                  
if __name__ == "__main__":
    
    main()


