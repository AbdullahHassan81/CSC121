# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 14:27:23 2025
@author: hassana5237
"""

#M2Lab
#Abdullah Hassan
#2/12/25
#CSC121
#used python tutor for help

def main():
    print("This program will be imported")

def eoq(demand, reorderCost, holdingCost, minOrder =0):
    

    # Calculate result
    eoq = (2 * demand * reorderCost / holdingCost) ** .5
    orderSize = max(eoq, minOrder) # account for the minimum order size

    # Display results
    print("\nEconomic Order Quantity:", round(eoq))
    print("Order Quantity:", orderSize)
    
    return eoq

# Calculate the EOQ - version 2: minimum order size
# Prompt for and get inputs
demand = float(input("Enter the projected demand (units/year): "))
reorderCost = float(input("Enter the reorder cost ($/order): "))
holdingCost = float(input("Enter the holding cost ($/year/unit): "))
minOrder = float(input("Enter the minimum order size (units/order): "))

eoq(demand, reorderCost, holdingCost, minOrder)

if __name__ == "__main__":
    main()
   
