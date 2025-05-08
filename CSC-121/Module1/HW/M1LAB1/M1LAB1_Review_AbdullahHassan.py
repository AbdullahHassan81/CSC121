# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#M1LAB1
#1/29/25
#Abdullah Hassan
#program that displays # of items and cost per item
quantity = float(input("Enter quantity or -1 to terminate: "))

while quantity !=-1 and quantity >=0:

    #evaluate 
    '''
    if quantity is >=15 - > 15%
    if > 10 -> 10%
    if >5 -> 5%
    '''
    
    if quantity > 15:
        
        discount = 0.15
    elif quantity > 10:
        
        discount = 0.1
    elif quantity > 5:
        
        discount = 0.05
    else: 
        discount = 0
        
    #determine pay
    result = (quantity * 4) - discount
    
    #display result 
    print("discount", discount)
    #print("Total $", format(result, '.2f'), sep = '')
    print(f"Total ${result:.2f}")
    quantity = float(input("Enter quantity or -1 to terminate"))


    