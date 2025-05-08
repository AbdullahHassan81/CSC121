# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 13:18:24 2025

@author: hassana5237
"""

def main():
    #program gets salaries for # of people 
    
    #ask for # of employees 
    emp_num = int(input("Enter number of employees: "))
    
    #start a loop that gets salary for each employee
    emp_info(emp_num)
    
    #call a funciton
def emp_info(employee_num):
    '''
    

    Parameters
    ----------
    employee_num : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''
with open('salaries.txt', 'w') as salaries:
    
    print(f'{"Name":<15}{"Salary"}', file=salaries)

    
    salaries.write(f'{"Name:<15"}{"Salary"}')
    print('-'*25)
    #print('-'*25+'\n')
    for num in range(employee_num):
        
            #get name and salary 
            print("\nInfo for Employee #", num+1)
            print()
            #get name and salary
            name = input("Enter employee name: ")
            salary = input("Enter " + name+"'s salary $")
            
            
main()
    
