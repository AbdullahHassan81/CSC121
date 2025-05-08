# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 14:10:13 2025

@author: seidih6290
"""
from pet import Pet


import pet_functions as pf


def main():
    
    choice = 0
    # menu driven program
    pets = []
    while choice != 4:
        
        pf.menu()
        print()
        # ask user for choice
        choice = int(input("Enter choice: "))
        print()
        
        # evaluate what was entered
        if choice == 1: 
            # read from file
            pets = pf.read(pets)

        elif choice == 2: 
            # new pets
            if len(pets) == 0:
                print('Read csv content first')
            else:
                pets = pf.new_info(pets)
        elif choice == 3: 
                # write all to file
                pf.write_info(pets)
        elif choice == 4:
            
            print('Program terminating')
        else:
            
            print("INVALID value entered!!")

main()
