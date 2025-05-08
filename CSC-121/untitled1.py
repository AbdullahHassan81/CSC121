# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 13:30:07 2025

@author: hassana5237
"""

name = 'jon'
salary = 3000

# 3 step process

# step 1, create variable that references file object

# here we tell the program the name of the file and how we want to work with it
#mode defines how we are going to work with the file (w = write, r = read, a= append)

file = open('practice.txt', 'w')
#step 2, process the info. if writing, use the writing methods 
# if one line, call the write() method
# if multiple lines(writelines)

# can only wrtie string, no numbers 
file.write('Susan' + '\n' + '2500')

file.write(name+'\n')# can only pass 1 arguement, must be a string 
file.write(f'{salary}')
#step 3 close the file

file.close