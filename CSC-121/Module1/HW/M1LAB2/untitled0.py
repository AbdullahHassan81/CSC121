# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 12:01:09 2025

@author: hassana5237
"""

# initialize smallest time
smallest_time = float('inf')  # set to infinity initially

# input to get the number of calculations
num_calculations = int(input("How many calculations do you want to perform? "))

# initialize counter
i = 0

# while loop to perform calculations
while i < num_calculations:
    # inputting to get the information for the calculation
    miles = float(input("What is the distance in miles? "))
    mph = int(input("What speed in mph? "))  # speed  
    time_in_hours = miles / mph 

    # calculating the total time in minutes 
    total_minutes = time_in_hours * 60  # convert hours to minutes 

    # print the results
    print(f"Speed: {mph} miles per hour")
    print(f"Total time in minutes: {total_minutes}")
    print(f"Total time in hours: {time_in_hours}")

    # update smallest time if current time is smaller
    if time_in_hours < smallest_time:
        smallest_time = time_in_hours

    # increment counter
    i += 1

# print the smallest time
print(f"The smallest time was: {smallest_time} hours")