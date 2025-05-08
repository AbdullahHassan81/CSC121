# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 13:34:31 2025

@author: hassana5237
"""

names = ['Jessica', 'Tom', 'Sandy']

for x in names:
        
    print("Good morning")
    
##new problem
nums = [5,7,6,10]

print(f'{"Num":<5}{"Sqr"}')
print("-"*10)

#for x in range(5,26,5): range only takes integers and you can do a decending order
#if you want to go down than add a - to it
for x in nums:
    sqr = x**2
    print(f'{x:<5}{sqr}')
    
##new problem
days = int(input("Enter num of days business operates: "))
print()

#accumulator var 
#print(f'{"Day:"<5}{"Amount"}')
#print("-"*15)

total = 0
for day in range(1, days+1);:
    amount = float(input("Enter amount generated for day #"+str(day)+"$"))
    #print(f'{day:<5}${amount:.2f}')
    total = total + amount 
print('Final profir generated $", total')