# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 17:22:22 2025

@author: someb
"""

# World Series winners 
# 7/9/25
# CSC121 m5Pro
# Abdullah Hassan


def menu():
    print("---------------Menu---------------")
    print("1) Display File Content")
    print("2) Search by Team (list number of times team won)")
    print("3) Search by Year")
    print("4) Create a file listing Teams and number of times they won")
    print("5) Exit")
    print("----------------------------------")

choice = 0  # assign it value thats not used
while choice != 5:
    menu()
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        try:
            with open('worldseries.txt', 'r') as file:
                # reads and prints the file 
                print(file.read())
        except FileNotFoundError:
            print("File 'worldseries.txt' not found.")
        
    elif choice == 2:
        try:
            with open('worldseries.txt', 'r') as file:
                content = file.readlines()  # Read all lines into a list
                team_name = input("Enter the name of the team (in lowercase letters): ").strip().lower()  # Get user input for team name
                found = False  # Flag to check if team was found
                years = []  # List to store winning years
                
                for line in content:
                    if team_name in line.lower():  # Check if the team name exists in the line (case-insensitive)
                        year = line.split()[0]  # Assuming the first word in the line is the year
                        years.append(year)  # Add winning year to the list
                        found = True
                
                if found:
                    print(f"The team '{team_name}' won in the following year(s): {', '.join(years)}")
                else:
                    print(f"The team '{team_name}' was not found in the file.")
        except FileNotFoundError:
            print("File 'worldseries.txt' not found.")
        
    elif choice == 3: 
        try:
            with open('worldseries.txt', 'r') as file:
                content = file.readlines()  # Read content here, not from choice 2
                # Initialize year variable
                year = input("Enter the year (1990-2022): ")
                
                # Validate the year
                if year.isdigit() and 1990 <= int(year) <= 2022:
                    found = False
                    
                    for line in content:
                        if line.startswith(year):  # Check if the line starts with the entered year
                            team = line.split()[1]  # Assuming the second word is the team name
                            print(f"The team that won in {year} is: {team}")
                            found = True
                            break
                    
                    if not found:
                        print(f"No team found for the year {year}.")
                else:
                    print("Invalid year. Please enter a year between 1990 and 2022.")
        except FileNotFoundError:
            print("File 'worldseries.txt' not found.")
            
    elif choice == 4: 
        try:
            with open('worldseries.txt', 'r') as file:
                content = file.readlines()  # Read content here
                
                # Create a dictionary to count wins per team
                team_wins = {}
                
                for line in content:
                    if line.strip():  # Skip empty lines
                        parts = line.split()
                        if len(parts) >= 2:  # Ensure line has at least 2 parts
                            team = parts[1]
                            if team in team_wins:
                                team_wins[team] += 1
                            else:
                                team_wins[team] = 1
                
                # Create the TXT file
                with open('Winners.txt', 'w') as txt_file:
                    txt_file.write("Team\tWins\n")  # Write title
                    for team, wins in team_wins.items():
                        txt_file.write(f"{team}\t{wins}\n")
                
                # Create the CSV file
                with open('Winners.csv', 'w') as csv_file:
                    csv_file.write("Team,Wins\n")  # Write title
                    for team, wins in team_wins.items():
                        csv_file.write(f"{team},{wins}\n")
                
                print("Files 'Winners.txt' and 'Winners.csv' have been created successfully.")
        except FileNotFoundError:
            print("File 'worldseries.txt' not found.")
    
    elif choice == 5:
        print("Goodbye!")

print("Program ended.")

'''
def menu():
    choice = 0 #assign it value thats not used
    while choice != 5:
        print("---------------Menu---------------")
        print("1) Display File Content")
        print("2) Search by Team (list number of times team won)")
        print("3) Search by Year")
        print("4) Create a file listing Teams and number of times they won")
        print("5) Exit")
        print("----------------------------------")
        
choice = 0 #assign it value thats not used
while choice != 5:
    menu()
    choice = int(input("Enter choice: "))
    
    if choice ==1:
        with open('worldseries.txt', 'r') as file:
            #reads and prints the file 
            print(file.read())
        
   
    elif choice == 2:
        with open('worldseries.txt', 'r') as file:
            content = file.readlines()  # Read all lines into a list
            team_name = input("Enter the name of the team (in lowercase letters): ").strip().lower()  # Get user input for team name
            found = False  # Flag to check if team was found
            years = []  # List to store winning years
            
            for line in content:
                if team_name in line.lower():  # Check if the team name exists in the line (case-insensitive)
                    year = line.split()[0]  # Assuming the first word in the line is the year
                    years.append(year)  # Add winning year to the list
                    found = True
            
            if found:
                print(f"The team '{team_name}' won in the following year(s): {', '.join(years)}")
            else:
                print(f"The team '{team_name}' was not found in the file.")
        
    elif choice ==3: 
        with open('worldseries.txt', 'r') as file:
            # Initialize year variable
           year = input("Enter the year (1990-2022): ")
           
           # Validate the year
           if year.isdigit() and 1990 <= int(year) <= 2022:
               found = False
               
               for line in content:
                   if line.startswith(year):  # Check if the line starts with the entered year
                       team = line.split()[1]  # Assuming the second word is the team name
                       print(f"The team that won in {year} is: {team}")
                       found = True
                       break
               
               if not found:
                   print(f"No team found for the year {year}.")
           else:
               print("Invalid year. Please enter a year between 1990 and 2022.")

    elif choice ==4: 
        with open('worldseries.txt', 'r') as file:
    
            # Create a dictionary to count wins per team
           team_wins = {}
           
           for line in content:
               team = line.split()[1]
               if team in team_wins:
                   team_wins[team] += 1
               else:
                   team_wins[team] = 1
           
           # Create the TXT file
           with open('Winners.txt', 'w') as txt_file:
               txt_file.write("Team\tWins\n")  # Write title
               for team, wins in team_wins.items():
                   txt_file.write(f"{team}\t{wins}\n")
           
           # Create the CSV file
           with open('Winners.csv', 'w') as csv_file:
               csv_file.write("Team,Wins\n")  # Write title
               for team, wins in team_wins.items():
                   csv_file.write(f"{team},{wins}\n")

    elif choice ==5:
        print("Exiting Program")
        # Close the file at the end to prevent resource leaks
        file.close()
'''