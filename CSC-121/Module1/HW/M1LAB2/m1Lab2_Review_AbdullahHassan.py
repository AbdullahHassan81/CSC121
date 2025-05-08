# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#m1Lab2
#2/6/25
#CSC121 m1Lab2Review
#Abdullah Hassan
#used python tutor
#variables 
shortest_minutes = 9999
more_routes = 'y' 
while more_routes == 'y':
 
 
    # inputting to get the information for the calculation
     
    miles = float(input("What is the distance in miles? "))
     
    mph = int(input("What speed in mph? "))#speed 
     
    time_in_hours = miles/mph 
     
    more_routes = input("More routes y/n ")
     
    # calculating the total time in minutes 
     
    total_minutes = time_in_hours * 60 # convert hours to minutes 
     
     
    # print the results
     
    print(f"Speed: {mph} miles per hour")
     
    print(f"Total time in minutes: {total_minutes}")
     
    print(f"Total time in hours: {time_in_hours}")
     
#finding the shortest time
     
if total_minutes < shortest_minutes:
     
        shortest_minutes = total_minutes
     
    #after the while loop
print(shortest_minutes, "is the shortest time")
