# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 13:34:33 2025

@author: moodyr1719
"""
import subtraction as sub
import addition as add

#Constants for menu choices
SUBTRACTION_ = 1 
ADDITION_ = 2
QUIT_CHOICE = 3

#main function
def main():
    #choice variable 
    choice = 0
    
    while choice != QUIT_CHOICE:
        #menu displayed
        display_menu()
    
        choice = int(input("Enter your choice: "))
    
        if choice ==SUBTRACTION_ :
            subVar = sub.subtraction()
        
        elif choice==2 :
            addVar = add.addition()
            
        elif choice ==3:
            print("Exitng the program")
            
        else:
            print("Error: Invalid Entry")
            
#display menu options
def display_menu():
    print('Menu')
    print("1 )SUBTRACTION_")
    print("2 )ADDITION_")
    print("3 )QUIT")
    

        
            
    
    